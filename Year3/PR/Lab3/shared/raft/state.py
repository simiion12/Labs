from enum import Enum
from typing import List, Dict, Optional
import time
from dataclasses import dataclass
import random


class ServerState(Enum):
    FOLLOWER = "FOLLOWER"
    CANDIDATE = "CANDIDATE"
    LEADER = "LEADER"

class RaftMessage(Enum):
    REQUEST_VOTE = "REQUEST_VOTE"
    VOTE_RESPONSE = "VOTE_RESPONSE"
    APPEND_ENTRIES = "APPEND_ENTRIES"

@dataclass
class LogEntry:
    term: int
    index: int
    data: dict

class RaftState:
    def __init__(self, node_id: str, nodes: List[str]):
        # Persistent state
        self.current_term: int = 0
        self.voted_for: Optional[str] = None
        self.log: List[LogEntry] = []

        # Volatile state
        self.state: ServerState = ServerState.FOLLOWER
        self.commit_index: int = 0
        self.last_applied: int = 0

        # Leader volatile state
        self.next_index: Dict[str, int] = {node: 0 for node in nodes}
        self.match_index: Dict[str, int] = {node: 0 for node in nodes}

        # Additional state
        self.node_id = node_id
        self.leader_id: Optional[str] = None
        self.nodes = nodes
        self.last_heartbeat = time.time()
        self.election_timeout = self._random_timeout()

        # Vote tracking for elections
        self.votes_received: set = set()


    def _random_timeout(self):
        """Generate a random election timeout between 150-300ms"""
        return random.uniform(0.15, 0.3)

    def reset_election_timeout(self):
        """Reset election timer with a new random timeout"""
        self.last_heartbeat = time.time()
        self.election_timeout = self._random_timeout()

    def start_election(self):
        """Initiate leader election"""
        self.state = ServerState.CANDIDATE
        self.current_term += 1
        self.voted_for = self.node_id
        self.votes_received = {self.node_id}
        self.reset_election_timeout()

    def receive_vote(self, voter_id: str, term: int):
        """Receive a vote from a node"""

        if term == self.current_term and self.state == ServerState.CANDIDATE:
            self.votes_received.add(voter_id)
            if len(self.votes_received) > len(self.nodes) // 2:
                self.become_leader()
                return True
            return False

    def become_leader(self):
        """Transition to leader state"""
        if self.state == ServerState.CANDIDATE:
            self.state = ServerState.LEADER
            self.leader_id = self.node_id
            # Initialize leader state
            self.next_index = {node: len(self.log) + 1 for node in self.nodes}
            self.match_index = {node: 0 for node in self.nodes}

    def become_follower(self, term: int):
        """Transition to follower state"""
        self.state = ServerState.FOLLOWER
        self.current_term = term
        self.voted_for = None
        self.reset_election_timeout()

    def can_grant_vote(self, candidate_id: str, term: int, last_log_index: int, last_log_term: int) -> bool:
        """
        Determine if this node can grant vote to candidate
        """
        if term < self.current_term:
            return False

        if (self.voted_for is None or self.voted_for == candidate_id) and term >= self.current_term:
            # Check if candidate's log is at least as up-to-date as ours
            my_last_term = self.log[-1].term if self.log else 0
            my_last_index = len(self.log) - 1 if self.log else 0

            if last_log_term > my_last_term:
                return True
            if last_log_term == my_last_term and last_log_index >= my_last_index:
                return True

        return False

    def handle_append_entries(self, term: int, leader_id: str) -> bool:
        """
        Handle append entries (or heartbeat)
        Returns True if the message was accepted
        """
        if term < self.current_term:
            return False

        if term > self.current_term:
            self.become_follower(term)

        self.leader_id = leader_id
        self.reset_election_timeout()
        return True

    def is_election_timeout(self) -> bool:
        """Check if election timeout has occurred"""
        return time.time() - self.last_heartbeat > self.election_timeout
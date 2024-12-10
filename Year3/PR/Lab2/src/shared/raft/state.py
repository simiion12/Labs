from enum import Enum
from typing import Optional, Set
import random
import time

from src.shared.raft.communication import Communication

class ServerState(Enum):
    FOLLOWER = "FOLLOWER"
    CANDIDATE = "CANDIDATE"
    LEADER = "LEADER"

class RaftMessage(Enum):
    REQUEST_VOTE = "REQUEST_VOTE"
    VOTE_RESPONSE = "VOTE_RESPONSE"
    APPEND_ENTRIES = "APPEND_ENTRIES"
    LEADER_UPDATE = "LEADER_UPDATE"
    HEARTBEAT = "HEARTBEAT"
    ALIVE = "ALIVE"

class RaftState:
    HEARTBEAT_INTERVAL = 1

    def __init__(self, server_id: str, nodes: dict):
        # Server identity
        self.server_id = server_id
        self.leader_id: Optional[str] = None

        # Election state
        self.current_term: int = 0
        self.voted_for: Optional[str] = None
        self.state = ServerState.FOLLOWER
        self.current_leader: Optional[str] = None
        self.votes_received: Set[str] = set()

        # Timeout management
        self.last_self_heartbeat = 0
        self.last_heartbeat = 0
        self.election_timeout = self._random_timeout()

        self.nodes = nodes
        self.http_port = self.nodes[self.server_id]["http_port"]

    def _random_timeout(self) -> float:
        """Generate random election timeout between 1.5 to 3 seconds"""
        return random.uniform(3, 6.0)

    def reset_election_timeout(self):
        """Reset the election timeout with a new random value"""
        self.election_timeout = self._random_timeout()

    def become_candidate(self):
        """Transition to candidate state"""
        self.state = ServerState.CANDIDATE
        self.current_term += 1
        self.voted_for = self.server_id
        self.votes_received = {self.server_id}
        self.reset_election_timeout()

    def become_follower(self, term: int):
        """Transition to follower state"""
        old_state = self.state
        self.state = ServerState.FOLLOWER
        self.current_term = term
        self.voted_for = None
        self.reset_election_timeout()
        if old_state == ServerState.LEADER:
            print(f"Stepping down from leader to follower in term {term}")

    def become_leader(self):
        """Transition to leader state"""
        if self.state == ServerState.CANDIDATE:
            self.state = ServerState.LEADER
            self.current_leader = self.server_id
            # Notify manager of new leadership
            print("Notifying manager of new leadership")
            Communication.notify_manager_of_leadership(self.server_id, self.http_port, self.current_term)
            # Clear votes after becoming leader
            self.votes_received.clear()
            self.last_heartbeat = time.time()


    def handle_heartbeat(self, term: int, leader_id: str) -> bool:
        """Handle received heartbeat"""
        if term < self.current_term:
            return False

        self.last_heartbeat = time.time()

        if (term >= self.current_term and
                (self.state == ServerState.LEADER or self.state == ServerState.CANDIDATE)):
            print(f"Stepping down: received heartbeat from {leader_id} in term {term}")
            self.become_follower(term)

        self.leader_id = leader_id
        return True

    def handle_vote_request(self, term: int, candidate_id: str) -> bool:
        """Handle vote request from candidate"""
        if term < self.current_term:
            return False
        if term > self.current_term or (self.voted_for is None or self.voted_for == candidate_id):
            self.become_follower(term)
            self.voted_for = candidate_id
            return True

        return False

    def handle_vote_response(self, term: int, voter_id: str, active_nodes) -> bool:
        """Handle vote response from other nodes"""
        if term < self.current_term:
            return False
        print("handle_vote_response", term, voter_id, active_nodes)
        if term >= self.current_term:
            self.votes_received.add(voter_id)
            if len(self.votes_received) > active_nodes // 2:
                self.become_leader()
                return True

        return False

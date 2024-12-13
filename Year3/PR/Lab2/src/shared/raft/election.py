import json
import time
from typing import Dict
import threading
import socket
import logging
import random

from src.shared.raft.state import RaftState, RaftMessage, ServerState
from src.shared.raft.communication import Communication

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - Node %(node_id)s: %(message)s'
)

ALIVE = 20


class Election:
    def __init__(self, server_id: str, udp_port: int, nodes: Dict[str, Dict[str, int]]):
        self.state = RaftState(server_id, nodes)
        self.udp_port = udp_port
        self.nodes = nodes

        # Add locks for thread synchronization
        self.state_lock = threading.Lock()  # For state changes
        self.active_nodes_lock = threading.Lock()  # For active_nodes dict

        # Initialize socket with proper binding
        self.udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.udp_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.udp_socket.bind(('0.0.0.0', udp_port))

        # Logger
        self.logger = logging.getLogger(__name__)
        self.logger = logging.LoggerAdapter(self.logger, {'node_id': server_id})

        # Communication
        self.comm = Communication({
            'nodes': self.nodes,
            'server_id': server_id
        })

        self.active_nodes = {}

        logging.info(f"Node {server_id} bound to UDP port {udp_port}")

    def _send_alive_heartbeat(self):
        while True:
            with self.active_nodes_lock:
                # Update alive status under lock
                self.active_nodes[self.state.server_id] = time.time()

            with self.state_lock:
                # Update heartbeat time under lock
                self.state.last_self_heartbeat = time.time()
                current_term = self.state.current_term

            self.comm.send_alive(current_term)

            time.sleep(10)

    def _send_leader_heartbeat(self):
        while True:
            with self.state_lock:
                is_leader = self.state.state == ServerState.LEADER
                current_term = self.state.current_term

            if is_leader:
                # Send heartbeat to all nodes, except self
                for node_id in self.nodes:
                    if node_id != self.state.server_id:
                        self.comm.send_heartbeat(current_term)

            time.sleep(4)

    def _run_election_loop(self):
        """Main election loop"""

        while True:
            with self.state_lock:
                current_time = time.time()
                current_state = self.state.state

                # Only check timeouts if we're not a leader
                if current_state != ServerState.LEADER:
                    time_since_heartbeat = current_time - self.state.last_heartbeat
                    timeout = self.state.election_timeout

                    # Check if we've passed both timeout and cooldown
                    print(time_since_heartbeat, "jjj", timeout , "jjj",current_time)
                    if time_since_heartbeat > timeout :
                        self.logger.info(f"Election timeout elapsed after {time_since_heartbeat:.2f} seconds")
                        self.state.become_candidate()
                        print(self.active_nodes, "Number of active nodes")
                        current_term = self.state.current_term

                        # Log state transition
                        self.logger.info(
                            f"State transition: {current_state} -> {self.state.state}, "
                            f"Term: {current_term}, Voted for: {self.state.voted_for}"
                        )

                        # Send vote request outside the lock
                        should_request_vote = True
                    else:
                        should_request_vote = False
                else:
                    should_request_vote = False

            if time_since_heartbeat > 50 and current_term > 10:
                should_request_vote = False
            # Send vote request outside the lock if needed
            if should_request_vote:
                self.comm.send_request_vote(current_term)

            time.sleep(6)

    def _handle_messages(self):
        """Handle incoming messages"""
        while True:
            data, addr = self.udp_socket.recvfrom(1024)
            message = json.loads(data.decode())

            if message["type"] == RaftMessage.ALIVE.value:
                with self.active_nodes_lock:
                    self.active_nodes[message['sender_id']] = time.time()

            elif message["type"] == RaftMessage.HEARTBEAT.value:
                with self.state_lock:
                    self.state.handle_heartbeat(message['term'], message['sender_id'])
                    self.logger.info(f"Received heartbeat from {message['sender_id']} for term {message['term']}")

            elif message["type"] == RaftMessage.REQUEST_VOTE.value:
                self.logger.info(f"Received vote request from {message['sender_id']} for term {message['term']}")
                should_send_vote = False
                current_term = None

                with self.state_lock:
                    if self.state.handle_vote_request(message['term'], message['sender_id']):
                        should_send_vote = True
                        self.logger.info(f"Voting for {message['sender_id']} in term {message['term']}")

                print(should_send_vote, "should_send_vote", message['term'])
                # Send vote response outside the lock
                if should_send_vote:
                    current_term = self.state.current_term
                    self.comm.send_vote_response(current_term, message['sender_id'])

            elif message["type"] == RaftMessage.VOTE_RESPONSE.value:
                with self.state_lock:
                    with self.active_nodes_lock:
                        active_node_count = len(self.active_nodes)
                    self.state.handle_vote_response(
                        message['term'],
                        message['sender_id'],
                        active_node_count
                    )
                    self.logger.info(
                        f"Received vote from {message['sender_id']} in term {message['term']}, "
                        f"Total votes: {len(self.state.votes_received)}"
                    )

    def _delete_inactive_nodes(self):
        """Count active nodes"""
        while True:
            time.sleep(ALIVE)
            current_time = time.time()

            with self.active_nodes_lock:
                inactive_nodes = [
                    node_id for node_id, last_heartbeat in self.active_nodes.items()
                    if current_time - last_heartbeat > ALIVE and node_id != self.state.server_id
                ]

                for node_id in inactive_nodes:
                    del self.active_nodes[node_id]
                    self.logger.info(f"Node {node_id} is inactive, removing from active nodes")

    def start(self):
        """Start election threads"""
        threads = [
            threading.Thread(target=self._run_election_loop, daemon=True),
            threading.Thread(target=self._handle_messages, daemon=True),
            threading.Thread(target=self._delete_inactive_nodes, daemon=True),
            threading.Thread(target=self._send_leader_heartbeat, daemon=True),
            threading.Thread(target=self._send_alive_heartbeat, daemon=True)
        ]

        for thread in threads:
            thread.start()
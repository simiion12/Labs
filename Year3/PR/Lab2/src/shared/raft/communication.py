import requests
import socket
import json
import logging
from enum import Enum

class RaftMessage(Enum):
    REQUEST_VOTE = "REQUEST_VOTE"
    VOTE_RESPONSE = "VOTE_RESPONSE"
    APPEND_ENTRIES = "APPEND_ENTRIES"
    LEADER_UPDATE = "LEADER_UPDATE"
    HEARTBEAT = "HEARTBEAT"
    ALIVE = "ALIVE"

class Communication:
    def __init__(self, socket_config):
        self.logger = logging.getLogger(__name__)
        self.logger = logging.LoggerAdapter(self.logger, {'node_id': socket_config['server_id']})

        self.udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.udp_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        # Don't bind here since this socket is only for sending

        self.nodes = socket_config['nodes']
        self.server_id = socket_config['server_id']

    def _broadcast(self, message_type: str, term: int, voter_for: str = None):
        message = {
            "type": message_type,
            "term": term,
            "sender_id": self.server_id
        }
        if voter_for:
            message["voter_for"] = voter_for

        for node_id, node in self.nodes.items():
            if node_id not in ["manager", self.server_id]:
                try:
                    # Use container name in raft_network
                    target_host = f'PR-Lab2-Node{node_id[-1]}'  # e.g., PR-Lab2-Node1
                    encoded_message = json.dumps(message).encode()
                    # logging.info(f"Node {self.server_id} sending {message_type} to {target_host}:{node['udp_port']}")
                    self.udp_socket.sendto(
                        encoded_message,
                        (target_host, node['udp_port'])
                    )
                except Exception as e:
                    logging.error(f"Broadcast error to {node_id} ({target_host}): {str(e)}")

    def send_alive(self, term: int):
        self._broadcast(RaftMessage.ALIVE.value, term)

    def send_heartbeat(self, term: int):
        self._broadcast(RaftMessage.HEARTBEAT.value, term)
        logging.info(f"Node {self.server_id} sent heartbeat")
        # if self.server_id == self.nodes.get('current_leader'):
        #     Communication.notify_manager_of_leadership(self.server_id, self.nodes[self.server_id]["http_port"])

    def send_request_vote(self, term: int):
        self._broadcast(RaftMessage.REQUEST_VOTE.value, term)

    def send_vote_response(self, term: int, voted_for: str):
        self._broadcast(RaftMessage.VOTE_RESPONSE.value, term, voted_for)

    @staticmethod
    def notify_manager_of_leadership(server_id: str, http_port: int, term: int):
        """Notify manager of new leadership"""
        try:
            response = requests.post(
                "http://PR-Web-Manager:7999/update_leader",
                params={
                    "server_id": server_id,
                    "port": http_port,
                    "term": term
                }
            )
            if response.status_code == 200:
                print(f"Successfully updated manager with new leader: {server_id}")
            else:
                print(f"Failed to update manager. Status: {response.status_code}")
        except Exception as e:
            print(f"Error notifying manager: {e}")
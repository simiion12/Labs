from typing import Dict
import socket
import json
import logging

from .state import RaftState, RaftMessage, ServerState


class Communication:
    def __init__(self, socket_config):
        self.logger = logging.getLogger(__name__)
        self.logger = logging.LoggerAdapter(self.logger, {'node_id': socket_config['server_id']})

        self.udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.udp_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
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
                    self.udp_socket.sendto(
                        json.dumps(message).encode(),
                        ('127.0.0.1', node["udp_port"])
                    )
                except Exception as e:
                    logging.error(f"Broadcast error to {node_id}: {e}")

    def send_alive(self, term: int):
        self._broadcast(RaftMessage.ALIVE.value, term)

    def send_heartbeat(self, term: int):
        self._broadcast(RaftMessage.HEARTBEAT.value, term)

    def send_request_vote(self, term: int):
        self._broadcast(RaftMessage.REQUEST_VOTE.value, term)

    def send_vote_response(self, term: int, voted_for: str):
        self._broadcast(RaftMessage.VOTE_RESPONSE.value, term, voted_for)

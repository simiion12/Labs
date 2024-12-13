import json
import time
from typing import Dict
import threading
import socket

from .state import RaftState, RaftMessage, ServerState
from .communication import Communication

import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - Node %(node_id)s: %(message)s'
)

ALIVE = 6

class Election:
    def __init__(self, server_id: str, udp_port: int, nodes: Dict[str, Dict[str, int]]):
        self.state = RaftState(server_id, nodes)
        self.udp_port = udp_port
        self.nodes = nodes

        # UDP socket
        self.udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.udp_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        # Logger
        self.logger = logging.getLogger(__name__)
        self.logger = logging.LoggerAdapter(self.logger, {'node_id': server_id})

        # Communication
        self.comm = Communication({
            'nodes': self.nodes,
            'server_id': server_id
        })

        self.active_nodes = {}

        try:
            self.udp_socket.bind(('127.0.0.1', self.udp_port))
            self.logger.info(f"Node started on UDP port {self.udp_port}")
        except Exception as e:
            print(f"Error binding socket: {e}")
            raise


    def start(self):
        """Start election threads"""
        threading.Thread(target=self._run_election_loop, daemon=True).start()
        threading.Thread(target=self._handle_messages, daemon=True).start()
        threading.Thread(target=self._delete_inactive_nodes, daemon=True).start()
        threading.Thread(target=self._one_node_handler(), daemon=True).start()


    def _run_election_loop(self):
        """Main election loop"""
        while True:
            # Maintaining alive status
            self.active_nodes[self.state.server_id] = time.time()
            self.state.last_self_heartbeat = time.time()

            # Send Alive message to all nodes
            for node_id in self.nodes:
                if node_id != self.state.server_id:
                    self.comm.send_alive(self.state.current_term)

            if self.state.state == ServerState.LEADER:
                # Send heartbeat to all nodes, except self
                for node_id in self.nodes:
                    if node_id != self.state.server_id:
                        self.comm.send_heartbeat(self.state.current_term)
            else:
                # Check if election timeout has elapsed
                if time.time() - self.state.last_heartbeat > self.state.election_timeout:
                    self.logger.info("Election timeout elapsed")
                    self.state.become_candidate()
                    self.comm.send_request_vote(self.state.current_term)
                    print(self.state.state)
            print(self.active_nodes, self.state.current_term, self.state.state)
            time.sleep(4)



    def _handle_messages(self):
        """Handle incoming messages"""
        while True:
            data, addr = self.udp_socket.recvfrom(1024)
            message = json.loads(data.decode())

            # counting active nodes
            if message["type"] == RaftMessage.ALIVE.value:
                self.active_nodes[message['sender_id']] = time.time()
            # Handling heartbeat from leader
            elif message["type"] == RaftMessage.HEARTBEAT.value:
                self.state.handle_heartbeat(message['term'], message['sender_id'])
            # Handling vote request
            elif message["type"] == RaftMessage.REQUEST_VOTE.value:
                if self.state.handle_vote_request(message['term'], message['sender_id']):
                    self.comm.send_vote_response(self.state.current_term, message['sender_id'])
            # Handling vote response
            elif message["type"] == RaftMessage.VOTE_RESPONSE.value:
                if not self.state.handle_vote_response(message['term'], message['sender_id'], len(self.active_nodes)):
                    self.state.become_follower(message['term'])


    def _delete_inactive_nodes(self):
        """Count active nodes"""
        while True:
            time.sleep(ALIVE)
            inactive_nodes = []
            for node_id, last_self_heartbeat in self.active_nodes.items():
                print(time.time() - last_self_heartbeat , ALIVE, "_delete_inactive_nodes", node_id)
                if time.time() - last_self_heartbeat > ALIVE:
                    inactive_nodes.append(node_id)
                    self.logger.info(f"DETECTED INACTIVE NODE: {node_id}")

            for node_id in inactive_nodes:
                del self.active_nodes[node_id]
                self.logger.info(f"Node {node_id} is inactive, removing from active nodes")


    def _one_node_handler(self):
        """Handle the case when there is only one node in the cluster"""
        time.sleep(10)
        if len(self.active_nodes) == 1:
            """Handle the case when there is only one node in the cluster"""
            self.state.become_leader()
            self.logger.info("Node is the only node in the cluster, becoming leader")
            while True:
                self.comm.send_heartbeat(self.state.current_term)

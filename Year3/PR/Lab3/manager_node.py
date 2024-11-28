import socket
import json
import threading
from typing import Dict
import logging
import time

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - Manager: %(message)s'
)


class ClusterManager:
    def __init__(self, udp_port: int):
        self.logger = logging.getLogger(__name__)
        self.udp_port = udp_port
        self.current_leader = None
        self.current_term = 0
        self.node_states = {}
        self.node_timeout = 5
        self.active_nodes = set()

        # UDP Socket setup
        self.udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.udp_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.udp_socket.bind(('127.0.0.1', self.udp_port))

        # Start message handling thread
        self.running = True
        self.message_thread = threading.Thread(target=self._handle_messages)
        self.message_thread.daemon = True
        self.message_thread.start()

        self.cleanup_thread = threading.Thread(target=self._cleanup_inactive_nodes)
        self.cleanup_thread.daemon = True
        self.cleanup_thread.start()

    def _handle_messages(self):
        self.logger.info("Manager started listening for cluster updates")
        while self.running:

            try:
                data, addr = self.udp_socket.recvfrom(1024)
                message = json.loads(data.decode())

                if message["type"] == "GET_STATUS":
                    # Send back cluster status
                    response = self.get_cluster_status()
                    self.udp_socket.sendto(
                        json.dumps(response).encode(),
                        addr
                    )
                elif message["type"] == "HEARTBEAT":
                    # Handle node heartbeat
                    node_id = message["node_id"]
                    self.node_states[node_id] = {
                        "state": "ACTIVE",
                        "last_update": time.time(),
                        "term": message.get("term"),
                        "role": message.get("role")
                    }
                    self.active_nodes.add(node_id)

                elif message["type"] == "LEADER_UPDATE":
                    new_leader = message["leader_id"]
                    term = message["term"]

                    if term >= self.current_term:
                        self.current_term = term
                        self.current_leader = new_leader
                        self.logger.info(f"New leader elected: {new_leader} (Term: {term})")

                elif message["type"] == "STATE_UPDATE":
                    node_id = message["node_id"]
                    state = message["state"]
                    self.node_states[node_id] = {
                        "state": state,
                        "last_update": time.time()
                    }
                    self.logger.info(f"Node {node_id} state update: {state}")

                    if node_id not in self.active_nodes:
                        self.logger.info(f"Node {node_id} became active again")
                    self.active_nodes.add(node_id)

            except Exception as e:
                self.logger.error(f"Error handling message: {e}")

    def _cleanup_inactive_nodes(self):
        while self.running:
            current_time = time.time()
            for node_id in list(self.active_nodes):
                if node_id in self.node_states:
                    last_update = self.node_states[node_id]["last_update"]
                    if current_time - last_update > self.node_timeout:
                        self.active_nodes.remove(node_id)
                        self.node_states[node_id]["state"] = "INACTIVE"
                        self.logger.warning(f"Node {node_id} marked as inactive")
            time.sleep(2)

    def get_cluster_status(self) -> Dict:
        return {
            "current_leader": self.current_leader,
            "current_term": self.current_term,
            "node_states": self.node_states,
            "active_nodes": list(self.active_nodes)
        }

    def stop(self):
        self.running = False
        self.udp_socket.close()
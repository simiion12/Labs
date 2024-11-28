from fastapi import FastAPI
import uvicorn
import time

from Labs.Year3.PR.Lab3.shared.raft.election import Election

# TODO: In json file
nodes = {
    "node1": {
        "udp_port": 5001,
        "http_port": 8001
    },
    "node2": {
        "udp_port": 5002,
        "http_port": 8002
    },
    "node3": {
        "udp_port": 5003,
        "http_port": 8003
    },
    "manager": {
        "udp_port": 5000,
        "http_port": 8000
    }
}

class WebServer:
    def __init__(self, http_port: int, udp_port: int, server_id: str):
        self.app = FastAPI()
        self.http_port = http_port
        self.udp_port = udp_port
        self.server_id = server_id
        self.setup_routes()
        # TODO: self.db = Database()

        self.election = Election(
            server_id=server_id,
            udp_port=udp_port,
            nodes=nodes
        )

        # TODO: Initialize the UDP election thread
        """
            self.election_thread = threading.Thread(
            target=self.election.start_handler,
            daemon=True
        )
        """

    def setup_routes(self):
        @self.app.get("/status")
        async def get_status():
            return {
                "server_id": self.server_id,
                "http_port": self.http_port,
                "udp_port": self.udp_port,
                "leader_id": self.election.state.current_leader,
                "current_term": self.election.state.current_term,
                "state": self.election.state.state.value
            }

    def run(self):
        #  # Start election process
        self.election.start()

        print(f"Starting server {self.server_id} on HTTP port {self.http_port} and UDP port {self.udp_port}")
        uvicorn.run(
            self.app,
            host="localhost",
            port=self.http_port
        )


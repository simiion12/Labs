from Labs.Year3.PR.Lab2.src.routes.car_routes import router as car_router
from Labs.Year3.PR.Lab2.src.routes.chat_routes import router as chat_router
from Labs.Year3.PR.Lab3.shared.raft.election import Election
from fastapi import FastAPI
import uvicorn
import threading


class ServerManager:
    def __init__(self, server_id: str, http_port: int, udp_port: int, nodes: dict):
        self.server_id = server_id
        self.http_port = http_port
        self.udp_port = udp_port
        self.nodes = nodes

        # Create election instance
        self.election = Election(
            server_id=server_id,
            udp_port=udp_port,
            nodes=nodes
        )

    def create_http_app(self):
        app = FastAPI()

        # Add LAB2 routes
        app.include_router(car_router)
        app.include_router(chat_router)

        # Add status endpoint for election
        @app.get("/status")
        async def get_status():
            return {
                "server_id": self.server_id,
                "http_port": self.http_port,
                "leader_id": self.election.state.current_leader,
                "current_term": self.election.state.current_term,
                "state": self.election.state.state.value
            }

        return app

    def run(self):
        # Create app
        app = self.create_http_app()

        # Start election thread
        election_thread = threading.Thread(
            target=self.election.start,
            daemon=True
        )
        election_thread.start()

        # Run server
        uvicorn.run(app, host="localhost", port=self.http_port)


# Usage in your run_web_server files:
def run_instance(instance_id: str):
    nodes = {
        "node1": {"udp_port": 5001, "http_port": 8002},
        "node2": {"udp_port": 5002, "http_port": 8003},
        "node3": {"udp_port": 5003, "http_port": 8004}
    }

    config = nodes[f"node{instance_id}"]
    server = ServerManager(
        server_id=f"node{instance_id}",
        http_port=config["http_port"],
        udp_port=config["udp_port"],
        nodes=nodes
    )
    server.run()
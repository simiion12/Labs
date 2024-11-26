from fastapi import FastAPI
import uvicorn

class WebServer:
    def __init__(self, http_port: int, udp_port: int, server_id: str):
        self.app = FastAPI()
        self.http_port = http_port
        self.udp_port = udp_port
        self.server_id = server_id
        self.setup_routes()
        # TODO: self.db = Database()
        # TODO: Initialize leader election
        """        
            self.election = LeaderElection(
            server_id=server_id,
            http_port=http_port,
            udp_port=udp_port
        )
        """
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
                "udp_port": self.udp_port
                # TODO: "leader_id": self.election.get_leader_id()
            }

    def run(self):
        # TODO: start the election thread and process

        uvicorn.run(
            self.app,
            host="localhost",
            port=self.http_port
        )


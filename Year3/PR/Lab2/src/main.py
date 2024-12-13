import os
from src.server_config import ServerManager
from src.routes.car_routes import router as car_router
from src.routes.chat_routes import router as chat_router
from src.shared.raft.election import Election
from fastapi import FastAPI

# Node configuration from environment
node_id = os.getenv('NODE_ID', 'node1')
udp_port = int(os.getenv('UDP_PORT', 5001))
http_port = int(os.getenv('HTTP_PORT', 8001))

# Election nodes configuration
nodes = {
    "node1": {"udp_port": 5001, "http_port": 8001},
    "node2": {"udp_port": 5002, "http_port": 8002},
    "node3": {"udp_port": 5003, "http_port": 8003}
}

# Create election instance
election = Election(
    server_id=node_id,
    udp_port=udp_port,
    nodes=nodes
)

# Create FastAPI app
app = FastAPI()

# Include routers
app.include_router(car_router)
app.include_router(chat_router)

# Optional: Add startup event to start election
@app.on_event("startup")
async def startup_event():
    # Start election in background
    election.start()
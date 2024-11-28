# manager/manager_server.py
from fastapi import FastAPI
import uvicorn
from manager_node import ClusterManager

# manager/manager_server.py
from fastapi import FastAPI
import uvicorn
from manager_node import ClusterManager

app = FastAPI()
manager = ClusterManager(udp_port=5000)  # Now using 5000

@app.get("/cluster/status")
async def get_cluster_status():
    return manager.get_cluster_status()

@app.get("/cluster/leader")
async def get_current_leader():
    return {"leader": manager.current_leader, "term": manager.current_term}

if __name__ == "__main__":
    try:
        uvicorn.run(app, host="127.0.0.1", port=8000)
    finally:
        manager.stop()
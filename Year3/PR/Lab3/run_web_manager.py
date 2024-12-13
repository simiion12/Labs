import uvicorn
from manager_node import ManagerNode
import threading

def main():
    manager = ManagerNode()
    app = manager.get_app()

    # Start manager threads in background
    manager_thread = threading.Thread(
        target=manager.start,
        daemon=True
    )
    manager_thread.start()

    # Run FastAPI app
    uvicorn.run(app, host="0.0.0.0", port=7999)

if __name__ == "__main__":
    main()
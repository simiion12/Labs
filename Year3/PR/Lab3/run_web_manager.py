from fastapi import FastAPI
import uvicorn
from manager_node import ManagerNode

app = FastAPI()
manager = ManagerNode()


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)

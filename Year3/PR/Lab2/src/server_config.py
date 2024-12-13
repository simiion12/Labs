import uvicorn
from fastapi import FastAPI
import threading


class ServerManager:
    @staticmethod
    def create_http_app() -> FastAPI:
        app = FastAPI()
        return app

    @staticmethod
    def create_ws_app() -> FastAPI:
        app = FastAPI()
        return app

    @staticmethod
    def run_server(app: FastAPI, host: str, port: int):
        uvicorn.run(app, host=host, port=port)

    @staticmethod
    def run_servers_threaded(http_app: FastAPI, ws_app: FastAPI):
        http_thread = threading.Thread(
            target=ServerManager.run_server,
            args=(http_app, "0.0.0.0", 8081)
        )

        ws_thread = threading.Thread(
            target=ServerManager.run_server,
            args=(ws_app, "0.0.0.0", 8071)
        )

        http_thread.start()
        ws_thread.start()

        return http_thread, ws_thread

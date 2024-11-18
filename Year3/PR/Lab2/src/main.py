from src.server_config import ServerManager
from src.routes.car_routes import router as car_router
from src.routes.chat_routes import router as chat_router


# Create HTTP app
http_app = ServerManager.create_http_app()
http_app.include_router(car_router)


# Create WebSocket app
ws_app = ServerManager.create_ws_app()
ws_app.include_router(chat_router)

# Run both servers
http_thread, ws_thread = ServerManager.run_servers_threaded(http_app, ws_app)
http_thread.join()
ws_thread.join()

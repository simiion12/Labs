from web_servers.server import WebServer
from web_servers.config import ServerConfig

if __name__ == "__main__":
    config = ServerConfig.for_server(2)
    server = WebServer(
        http_port=config.http_port,
        udp_port=config.udp_port,
        server_id=config.server_id
    )
    server.run()

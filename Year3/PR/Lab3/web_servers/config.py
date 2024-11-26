class ServerConfig:
    def __init__(self, server_id: str, http_port: int, udp_port: int):
        self.server_id = server_id
        self.http_port = http_port
        self.udp_port = udp_port

    @classmethod
    def for_server(cls, server_num: int):
        return cls(
            server_id=f"server_{server_num}",
            http_port=8000 + server_num,
            udp_port=5000 + server_num
        )

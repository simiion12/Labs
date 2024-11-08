# main.py
import asyncio
import threading
from fastapi import FastAPI, WebSocket
from fastapi.responses import HTMLResponse
from src.routes.car_routes import router as car_router
from src.chat.tcp_server.tcp_server import TCPServer
from src.chat.chat_room.websocket_handler import WebSocketHandler
from src.chat.file_coordination.file_handler import FileHandler


app = FastAPI()
file_handler = FileHandler()
websocket_handler = None
tcp_server = None

app.include_router(car_router)


def run_tcp_server():
    """Run TCP server in a separate thread"""
    global tcp_server
    tcp_server = TCPServer(file_handler, websocket_handler)
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(tcp_server.run())


@app.on_event("startup")
async def startup_event():
    global websocket_handler
    # Initialize WebSocket handler
    websocket_handler = WebSocketHandler(file_handler)

    # Start TCP server in a separate thread
    tcp_thread = threading.Thread(target=run_tcp_server)
    tcp_thread.daemon = True
    tcp_thread.start()


@app.websocket("/chat")
async def websocket_endpoint(websocket: WebSocket):
    await websocket_handler.handle_client(websocket)


# Modified HTML page with better message display
@app.get("/")
async def get_chat_page():
    return HTMLResponse("""
    <html>
        <head>
            <title>Chat Room</title>
            <style>
                body {
                    font-family: Arial, sans-serif;
                    max-width: 800px;
                    margin: 0 auto;
                    padding: 20px;
                }
                #status {
                    padding: 10px;
                    margin: 10px 0;
                    border-radius: 5px;
                }
                .connected {
                    background-color: #dff0d8;
                    color: #3c763d;
                }
                .disconnected {
                    background-color: #f2dede;
                    color: #a94442;
                }
                #chat-box {
                    height: 400px;
                    border: 1px solid #ccc;
                    margin: 10px 0;
                    padding: 10px;
                    overflow-y: auto;
                }
                .message {
                    margin: 5px 0;
                    padding: 5px;
                    border-radius: 3px;
                }
                .tcp-message {
                    background-color: #e3f2fd;
                }
                .websocket-message {
                    background-color: #f5f5f5;
                }
                .file-operation {
                    background-color: #fff3e0;
                }
                .controls {
                    display: flex;
                    gap: 10px;
                    margin: 10px 0;
                }
                button {
                    padding: 8px 16px;
                    border: none;
                    border-radius: 4px;
                    background-color: #4CAF50;
                    color: white;
                    cursor: pointer;
                }
                button:hover {
                    background-color: #45a049;
                }
                input {
                    flex-grow: 1;
                    padding: 8px;
                    border: 1px solid #ccc;
                    border-radius: 4px;
                }
            </style>
        </head>
        <body>
            <h1>Chat Room</h1>
            <div id="status" class="disconnected">Disconnected</div>
            <div id="chat-box"></div>
            <div class="controls">
                <input type="text" id="messageInput" placeholder="Type your message">
                <button onclick="sendMessage()">Send Message</button>
                <button onclick="sendRead()">Read File</button>
                <button onclick="sendWrite()">Write to File</button>
            </div>

            <script>
                let ws;

                function connect() {
                    ws = new WebSocket('ws://localhost:8000/chat');

                    ws.onopen = function() {
                        document.getElementById('status').className = 'connected';
                        document.getElementById('status').textContent = 'Connected';
                    };

                    ws.onclose = function() {
                        document.getElementById('status').className = 'disconnected';
                        document.getElementById('status').textContent = 'Disconnected - Reconnecting...';
                        setTimeout(connect, 1000);
                    };

                    ws.onmessage = function(event) {
                        const chatBox = document.getElementById('chat-box');
                        const messageDiv = document.createElement('div');
                        messageDiv.className = 'message';

                        // Add specific styling based on message type
                        if (event.data.includes('TCP Client')) {
                            messageDiv.classList.add('tcp-message');
                        } else if (event.data.includes('File content') || event.data.includes('wrote')) {
                            messageDiv.classList.add('file-operation');
                        } else {
                            messageDiv.classList.add('websocket-message');
                        }

                        messageDiv.textContent = event.data;
                        chatBox.appendChild(messageDiv);
                        chatBox.scrollTop = chatBox.scrollHeight;
                    };
                }

                function sendMessage() {
                    const input = document.getElementById('messageInput');
                    if (input.value) {
                        ws.send(input.value);
                        input.value = '';
                    }
                }

                function sendRead() {
                    ws.send('read');
                }

                function sendWrite() {
                    const input = document.getElementById('messageInput');
                    if (input.value) {
                        ws.send('write:' + input.value);
                        input.value = '';
                    } else {
                        alert('Please enter text to write to the file');
                    }
                }

                // Connect when page loads
                connect();

                // Handle Enter key in input field
                document.getElementById('messageInput').addEventListener('keypress', function(e) {
                    if (e.key === 'Enter') {
                        sendMessage();
                    }
                });
            </script>
        </body>
    </html>
    """)
from fastapi import FastAPI
import asyncio
from fastapi.responses import FileResponse
import os
from src.routes.car_routes import router as car_router
from src.chat.tcp_server.tcp_server import TCPServer
from src.chat.chat_room.websocket_handler import WebSocketHandler
from fastapi import FastAPI, Request, WebSocket
from fastapi.responses import HTMLResponse
app = FastAPI(debug=True)

app.include_router(car_router)

@app.on_event("startup")
async def startup_event():
    # Start the WebSocket handler
    app.state.websocket_handler = WebSocketHandler()
    app.state.websocket_handler_task = asyncio.create_task(app.state.websocket_handler.run())

@app.on_event("shutdown")
async def shutdown_event():
    # Stop the WebSocket handler
    app.state.websocket_handler_task.cancel()
    await app.state.websocket_handler_task

# @app.get("/", response_class=HTMLResponse)
# async def root():
#     file_path = os.path.join("templates", "chat_room.html")
#     return FileResponse("Labs/Year3/PR/Lab2/src/templates/chat_room.html")
@app.get("/", response_class=HTMLResponse)
async def root():
    return """
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

                h1 {
                    color: #333;
                    text-align: center;
                }

                #chat-messages {
                    height: 300px;
                    overflow-y: scroll;
                    border: 1px solid #ccc;
                    padding: 10px;
                    margin-bottom: 20px;
                    background: #f9f9f9;
                }

                .message {
                    margin: 5px 0;
                    padding: 5px;
                    border-radius: 5px;
                }

                .input-container {
                    display: flex;
                    gap: 10px;
                    margin-bottom: 10px;
                }

                input {
                    flex-grow: 1;
                    padding: 8px;
                    border: 1px solid #ccc;
                    border-radius: 4px;
                }

                button {
                    padding: 8px 15px;
                    background-color: #4CAF50;
                    color: white;
                    border: none;
                    border-radius: 4px;
                    cursor: pointer;
                }

                button:hover {
                    background-color: #45a049;
                }

                .file-controls {
                    display: flex;
                    gap: 10px;
                    margin-bottom: 10px;
                }

                .file-controls button {
                    flex: 1;
                }

                #read-btn {
                    background-color: #2196F3;
                }

                #read-btn:hover {
                    background-color: #1976D2;
                }
            </style>
            <script>
                let socket;

                function connectToChat() {
                    socket = new WebSocket("ws://localhost:8000/chat");

                    socket.onopen = () => {
                        console.log("Connected to chat room");
                        addSystemMessage("Connected to chat room");
                    };

                    socket.onmessage = (event) => {
                        const chatMessages = document.getElementById("chat-messages");
                        const newMessage = document.createElement("div");
                        newMessage.className = "message";

                        // Check if the message is from file operations
                        if (event.data.startsWith("File content:") || event.data.startsWith("Wrote")) {
                            newMessage.style.backgroundColor = "#e3f2fd";
                        } else {
                            newMessage.style.backgroundColor = "#f0f0f0";
                        }

                        newMessage.textContent = event.data;
                        chatMessages.appendChild(newMessage);
                        chatMessages.scrollTop = chatMessages.scrollHeight;
                    };

                    socket.onclose = () => {
                        console.log("Disconnected from chat room");
                        addSystemMessage("Disconnected from chat room");
                    };
                }

                function addSystemMessage(message) {
                    const chatMessages = document.getElementById("chat-messages");
                    const newMessage = document.createElement("div");
                    newMessage.className = "message";
                    newMessage.style.backgroundColor = "#ffebee";
                    newMessage.textContent = message;
                    chatMessages.appendChild(newMessage);
                }

                function sendMessage() {
                    const messageInput = document.getElementById("message-input");
                    const message = messageInput.value.trim();
                    if (message) {
                        socket.send(message);
                        messageInput.value = "";
                    }
                }

                function readFile() {
                    socket.send("read");
                }

                function writeToFile() {
                    const messageInput = document.getElementById("message-input");
                    const message = messageInput.value.trim();
                    if (message) {
                        socket.send(`write:${message}`);
                        messageInput.value = "";
                    } else {
                        alert("Please enter a message to write to the file");
                    }
                }

                // Handle Enter key in input field
                document.addEventListener('DOMContentLoaded', function() {
                    const messageInput = document.getElementById("message-input");
                    messageInput.addEventListener("keypress", function(event) {
                        if (event.key === "Enter") {
                            sendMessage();
                        }
                    });
                });
            </script>
        </head>
        <body onload="connectToChat()">
            <h1>Chat Room</h1>
            <div class="file-controls">
                <button id="read-btn" onclick="readFile()">Read from File</button>
                <button onclick="writeToFile()">Write to File</button>
            </div>
            <div id="chat-messages"></div>
            <div class="input-container">
                <input type="text" id="message-input" placeholder="Type your message" />
                <button onclick="sendMessage()">Send</button>
            </div>
        </body>
    </html>
"""

@app.websocket("/chat")
async def websocket_endpoint(websocket: WebSocket):
    await app.state.websocket_handler.handle_client(websocket)
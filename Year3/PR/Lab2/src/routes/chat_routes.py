from fastapi import APIRouter, WebSocket, WebSocketDisconnect, HTTPException, status
from fastapi.responses import HTMLResponse
import logging

from src.manager import ChatRoom


logger = logging.getLogger(__name__)


router = APIRouter(
    prefix="/chat",
    tags=["chat"],
)

chat_room = ChatRoom()

@router.websocket("/ws/{client_id}")
async def websocket_endpoint(websocket: WebSocket, client_id: str):
    try:
        await chat_room.connect(websocket, client_id)

        # Send chat history to new client
        for message in chat_room.messages[-50:]:
            await websocket.send_text(message)

        while True:
            message = await websocket.receive_text()
            await chat_room.broadcast(f"Client {client_id}: {message}")

    except WebSocketDisconnect:
        chat_room.disconnect(client_id)
        await chat_room.broadcast(f"Client {client_id} left the chat")
    except Exception as e:
        logger.error(f"Error in websocket connection: {e}")
        chat_room.disconnect(client_id)


@router.get("/active-users")
async def get_active_users():
    """Get list of active chat users"""
    try:
        return {"active_users": list(chat_room.get_active_clients())}
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"An error occurred: {str(e)}"
        )


@router.get("/message-history")
async def get_message_history():
    """Get chat message history"""
    try:
        return {"messages": chat_room.messages[-50:]}
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"An error occurred: {str(e)}"
        )


@router.get("/{username}", response_class=HTMLResponse)
async def get_chat_client(username: str):
    """Get chat client HTML page"""
    try:
        # Get template and replace username
        with open("/app/src/static/chat.html", 'r') as file:
            template = file.read()
        html_content = template.replace("{username}", username)

        return HTMLResponse(content=html_content, media_type="text/html")

    except Exception as e:
        logger.error(f"Error serving chat client: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"An error occurred: {str(e)}"
        )


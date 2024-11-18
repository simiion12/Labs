# tcp_client.py
import asyncio
import sys


async def tcp_client():
    try:
        # Connect to the TCP server
        reader, writer = await asyncio.open_connection('127.0.0.1', 8001)
        print("Connected to TCP server")

        while True:
            # Get input from user
            message = input("Enter command (write:message or read, or 'quit' to exit): ")

            if message.lower() == 'quit':
                break

            # Send message to server
            writer.write(message.encode())
            await writer.drain()

            # Get response from server
            data = await reader.read(1024)
            response = data.decode()
            print(f"Received: {response}")

    except ConnectionRefusedError:
        print("Could not connect to server. Make sure the server is running.")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        if 'writer' in locals():
            writer.close()
            await writer.wait_closed()


if __name__ == "__main__":
    asyncio.run(tcp_client())
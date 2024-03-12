import asyncio
import time
from aiohttp import ClientSession
from sys import argv

seconds = int(argv[1])
async def websocket_client():
    uri = "http://localhost:8765/"
    async with ClientSession() as session:
        async with session.ws_connect(uri) as ws:
            start_time = time.time()
            messages_sent = 0
            while True:
                await ws.send_str(f"Message {messages_sent}")
                response = await ws.receive_str()
                messages_sent += 1
                if time.time() - start_time >= seconds:
                    break
            print(f"Messages sent: {messages_sent} messages/s")

if __name__ == '__main__':
    asyncio.run(websocket_client())  # Adjust the message rate as needed

import asyncio
import time
from aiohttp import ClientSession
from sys import argv

async def websocket_client():
    uri = "http://localhost:8765/"
    async with ClientSession() as session:
        async with session.ws_connect(uri) as ws:
            start_time = time.time()
            for i in range(int(argv[1])):  # Adjust the number of messages as needed
                await ws.send_str(f"Message {i}")
                response = await ws.receive_str()
                #print(f"Received response: {response}")
            end_time = time.time()
            total_time = end_time - start_time
            print(f"Total time taken: {total_time} seconds")
            print(f"Average latency: {total_time / 100} seconds")  # Adjust this based on the number of messages

if __name__ == '__main__':
    asyncio.run(websocket_client())

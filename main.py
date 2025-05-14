import asyncio
from client import Client
from mock_api import MockApi

async def main():
    client = Client()
    client_task = asyncio.create_task(client.begin())

    api = MockApi()
    api_task = asyncio.create_task(api.get("basic"))

    while True:
        await asyncio.sleep(5)
        client_task.cancel()
    

if __name__ == "__main__":
    asyncio.run(main())
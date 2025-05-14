import asyncio
from core.client import Client
from core.mock_api import MockApi

async def main():
    api = MockApi()

    client = Client()
    client_task = asyncio.create_task(client.begin())

    while True:
        await asyncio.sleep(5)
        client_task.cancel()
    

if __name__ == "__main__":
    asyncio.run(main())
from asyncio import wait
from mock_api import MockApi

api = MockApi()

def main():
    print(
    api.get('basic'),
    api.get('img1'),
    api.get('img2'),
    api.get('more')
    )
    


main()
from asyncio import wait
from mock_api import MockApi

api = MockApi()

def main():
    response = api.get('basic')
    print(response)


main()
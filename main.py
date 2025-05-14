from mock_api import MockApi
from client import Client

api = MockApi()

def main():
    client = Client()
    client.begin()

if __name__ == "__main__":
    main()
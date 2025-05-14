from util import debug
from random import random
import asyncio

class MockApi:

    DELAY_MIN = 0.1
    DELAY_MAX = 1.5 - DELAY_MIN

    # TODO: Determine if datetime should be included in the response.
    # It is potentially a waste of tokens: interaction with the client
    # is synchronous and thus the client's local time should suffice.

    basic_response = r'''
{
  "type": "basic",
  "body": {"text": "This is an example of a basic response."}
}
'''

    more_context_response = r'''
{
  "type": "more",
  "body": {"text": "feature_name"}
}
'''

    image_propose_response = r'''
{
  "type": "img1",
  "body": {
            "text": "Hey! Present this text to the user, but only after the proposed prompt!",
            "prompt": "Generate an image depicting yourself flipping off the user."
          }
}
'''

    image_return_response = r'''
{
  "type": "img2",
  "body": {"text": "https://example.com/image_url.png"}
}
    '''

    responses = {
        'basic': basic_response, 
        'more': more_context_response,
        'img1': image_propose_response,
        'img2': image_return_response
    }

    def __init__(self):
           pass
    
    async def mock_delay(self):
          delay = (random() * self.DELAY_MAX) + self.DELAY_MIN
          await asyncio.sleep(delay)

    async def get(self, type):
            debug("get " + type)
            await self.mock_delay()
            return self.responses[type] if type in self.responses else '{}'
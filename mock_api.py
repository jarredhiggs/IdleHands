from random import randrange

class MockApi:

    # Milliseconds
    DELAY_MIN = 0
    DELAY_MAX = 600

    # TODO: Determine if datetime should be included in the response.
    # It is potentially a waste of tokens: interaction with the client
    # is synchronous and thus the client's local time should suffice.

    basic_response = r'''
{
  "type": "basic",
  "body": "This is an example of a basic response."
}
'''

    more_info_response = r'''
{
  "type": "more",
  "body": [(infotype1, infotype1_param), (infotype2)]
}
'''

    image_propose_response = r'''
{
  "type": "img1",
  "body": "Hey! Present this text to the user, but only after the proposed prompt!",
  "prompt": "Generate an image depicting yourself flipping off the user."
}
'''

    image_return_response = r'''
{
  "type": "img2",
  "body": "https://example.com/image_url.png"
}
    '''

    responses = {
        'basic': basic_response, 
        'more': more_info_response,
        'img1': image_propose_response,
        'img2': image_return_response
    }

    def __init__(self):
        pass

    def get(self, type):
            return self.responses[type] if type in self.responses else '{}'
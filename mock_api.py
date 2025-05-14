import collections
from datetime import datetime

class MockApi:

    raw_response = r'''
{
  "datetime": ''' + str(datetime.now()) + r'''
  "response_text": "This is an example of the API's response text which we will be processing and analyzing. Yep."
  "more_info": [(infotype1, infotype1_param), (infotype2)]
  "image_url": http://www.example.com/image_url.png
}
'''

    def __init__(self):
        print(self.raw_response)

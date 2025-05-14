import asyncio
from util import debug as d

class Client:
    def __configure_parameters(self, parameters = None):
        required_params = ["check_duration", "text_timeout", "image_timeout"]

        try:
            if parameters is None:        
                from config import config
                params = config["client"]          
            else:
                params = parameters
            
            # Check that every required parameter is defined
            [params[x] for x in required_params]

        except:
               raise "No valid config available for Client!"
    

    async def __main_loop(self):
        while True:
            d("Beginning of Main Loop")
            await asyncio.sleep(0.5)
    
    def begin(self):
        asyncio.run(self.__main_loop())

    def __init__(self):
        self.__configure_parameters()
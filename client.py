import asyncio
from util import debug

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
        
        self.params = params

    async def __main_loop(self):
        while True:
            debug("Beginning of Main Loop")
            await asyncio.sleep(self.params['check_duration'])
    
    async def begin(self):
        await self.__main_loop()

    def __init__(self):
        self.__configure_parameters()
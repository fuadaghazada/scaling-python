## Import other libraries if you want (asyncio and aiohttp are supported)
import time
import asyncio
import aiohttp

urls = ["http://educative.io", "http://educative.io/blog", "http://youtube.com"]

##########################################
### Start your code here

async def get(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return response

loop = asyncio.get_event_loop()
results = loop.run_until_complete(
        asyncio.gather(*[get(url) for url in urls])
    )

### End code here
##########################################
print("Results: %s" % results)
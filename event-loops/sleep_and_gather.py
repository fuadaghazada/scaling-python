import asyncio

async def hello_world():
    print("hello world!")
    await asyncio.sleep(1)
    return 1

async def hello_python():
    print("hello Python!")
    await asyncio.sleep(2)
    return 2

event_loop = asyncio.get_event_loop()
try:
    result = event_loop.run_until_complete(asyncio.gather(
        hello_python(),
        hello_world(),
    ))
    print(result)
finally:
    event_loop.close()
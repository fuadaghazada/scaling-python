import asyncio

def hello_world():
    print("Hello World")

event_loop = asyncio.get_event_loop()
event_loop.call_later(1, hello_world)
event_loop.run_forever()
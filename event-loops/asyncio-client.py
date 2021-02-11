import asyncio

SERVER_ADDRESS = ('0.0.0.0', 1234)


class EchoClientProtocal(asyncio.Protocol):
    def __init__(self, message, loop):
        self.message = message
        self.loop = loop
    
    def talk(self):
        print("Message:", self.message)
        self.transport.write(self.message)
    
    def connection_made(self, transport):
        self.transport = transport
        self.talk()
    
    def data_received(self, data):
        self.talk()

    def connection_lost(self, exc):
        self.loop.stop()
    

event_loop = asyncio.get_event_loop()
factory = event_loop.create_connection(lambda: EchoClientProtocal(b'Hello World', event_loop), *SERVER_ADDRESS)
event_loop.run_until_complete(factory)

try:
    event_loop.run_forever()
finally:
    event_loop.close()
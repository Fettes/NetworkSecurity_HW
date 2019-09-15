import asyncio

class EchoClientProtocol(asyncio.Protocol):
    def __init__(self,loop):
        self.loop = loop
        self.sendindex = 0

    def connection_made(self,transport):
        print("*")
        self.transport= transport

    def data_received(self,data):
        print(data)
        readytosent = [
               # "RESULT,35ae1a780e4b27c66859607d136d99c053745193448399a264927cf5f244e6f8",
            "SUBMIT, Zichen Wang, zwang216@jhu.edu, 6, 3456",
            "look<EOL>\n",
            "look mirror<EOL>\n",
            "get hairpin<EOL>\n",
            "look chest<EOL>\n",
            "unlock chest with hairpin<EOL>\n",
            "open chest<EOL>\n",
            "look in chest<EOL>\n",
            "get hammer from chest<EOL>\n",
            "unlock door with hairpin<EOL>\n",
            "open door<EOL>\n"
        ]
        if (self.sendindex < 11):
            self.transport.write(readytosent[self.sendindex].encode())
            self.sendindex = self.sendindex + 1
    
loop = asyncio.get_event_loop()

conn = loop.create_connection(lambda: EchoClientProtocol(loop),'192.168.200.52',19003)

loop.run_until_complete(conn)
loop.run_forever()
loop.close()

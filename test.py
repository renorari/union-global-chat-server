from websockets import connect
import zlib
import asyncio
from orjson import loads


async def main():
    async with connect("ws://localhost:8080/gateway") as ws:
        print(loads(zlib.decompress(await ws.recv())))
        await ws.send(zlib.compress(b'{"type": "identify", "token": "yHogyE4a7nYy3kQXgt3cpLoz12HgCKDw"}'))
        while True:
            print(loads(zlib.decompress(await ws.recv())))


asyncio.run(main())
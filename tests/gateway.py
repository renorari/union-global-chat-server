from websockets import connect
import zlib
import asyncio
from orjson import loads


async def main():
    async with connect("ws://localhost:8080/api/v1/gateway") as ws:
        print(loads(zlib.decompress(await ws.recv())))
        await ws.send(zlib.compress(b'{"type": "identify", "token": "ik8J6D4qRggWkWBVzti07feetHNh2USP"}'))
        while True:
            print(loads(zlib.decompress(await ws.recv())))


asyncio.run(main())
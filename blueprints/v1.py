from sanic import Blueprint, response
from lib import authorized
from tinydb import TinyDB, Query
from orjson import dumps, loads
from types import Content
import asyncio
import zlib


bp = Blueprint("version_1", url_prefix="/api/v1")

db = TinyDB('db.json')
user = Query()

def dumper(data):
    return zlib.compress(dumps(data))
wss = []

class HeartBeat:
    def __init__(self, ws):
        self.ws = ws

    async def send_heartbeat(self):
        await self.ws.send(dumper({'type': 'heartbeat'}))

    async def sending_heartbeat(self):
        while True:
            try:
                await self.send_heartbeat()
            except Exception:
                wss.remove(self.ws)
                break
            await asyncio.sleep(10)

@bp.websocket("/gateway")
async def gateway(request, ws):
    """
    The gateway is the main connection point between the client and the server.
    It is responsible for receiving the client's messages and sending them to
    the right place.
    """
    await ws.send(dumper({"type": "hello"}))
    while True:
        data = loads(zlib.decompress(await ws.recv()))
        if data["type"] == "identify":
            token = db.search(user.token == data["token"])
            if len(token) == 0:
                await ws.send(dumper({"type": "identify", "success": False}))
                await ws.close()
            else:
                await ws.send(dumper({"type": "identify", "success": True}))
                wss.append(ws)
                app.loop.create_task(HeartBeat(ws).sending_heartbeat())

@bp.post("/channels")
@authorized()
async def send(request, userid):
    data: Content = request.json
    payload = {
        "type": "send",
        "data": {
            "from": userid,
            "data": data
        }
    }
    for ws in wss:
        await ws.send(dumper(payload))
    return response.json({"success": True})
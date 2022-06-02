from typing import TypedDict
from orjson import loads

class Config(TypedDict):
    host: str
    port: int

with open("config.json", "r") as f:
    config: Config = loads(f.read())
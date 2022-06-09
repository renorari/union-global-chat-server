from sanic import response


def json(data: dict=None, *, message: str=None,
         status: int=200):
    success = True
    if status != 200:
        success = False
    return response.json({"success": success, "status": status, "message": message, "data": data})

from functools import wraps
from tinydb import TinyDB, Query
from sanic import response

db = TinyDB('db.json')
user = Query()

def authorized():
    def decorator(f):
        @wraps(f)
        async def decorated_function(request, *args, **kwargs):
            s = db.search(user.token == request.token)
            if len(s) == 0:
                return response.json({"success": False}, status=401)
            else:
                return await f(request, s[0]["user"], *args, **kwargs)
        return decorated_function
    return decorator
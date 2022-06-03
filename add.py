import random, string
from tinydb import TinyDB

db = TinyDB('db.json')
table = db.table("token")

def randomname(n):
   return ''.join(random.choices(string.ascii_letters + string.digits, k=n))

user = input("userid: ")
token = randomname(32)
table.insert({'user': user, 'token': token})
print(f"Created user {user} with token {token}")
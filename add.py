import random, string
from tinydb import TinyDB

db = TinyDB('db.json')

def randomname(n):
   return ''.join(random.choices(string.ascii_letters + string.digits, k=n))

user = input("userid: ")
token = randomname(32)
db.insert({'user': user, 'token': token})
print(f"Created user {user} with token {token}")
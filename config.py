import os

API_ID = int(os.environ.get("API_ID", 20718334))
API_HASH = os.environ.get("API_HASH", 4e81464b29d79c58d0ad8a0c55ece4a5)
BOT_TOKEN = os.environ.get("BOT_TOKEN", 6717070197:AAEJ57hiERZxqv6bQaTKSfsey_wTqF_RQbA)
DB_CHANNEL_ID = os.environ.get("100217733494")
IS_PRIVATE = os.environ.get("IS_PRIVATE",true) # any input is ok But True preferable
OWNER_ID = int(os.environ.get("7432102513"))
UPDATE_CHANNEL = os.environ.get('UPDATE_CHANNEL', '-1002072642438')
AUTH_USERS = list(int(i) for i in os.environ.get("AUTH_USERS", "5585016974").split(" ")) if os.environ.get("AUTH_USERS") else []
if OWNER_ID not in AUTH_USERS:
    AUTH_USERS.append(5585016974)

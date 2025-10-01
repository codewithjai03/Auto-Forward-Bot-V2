from os import environ 

class Config:
    API_ID = environ.get("API_ID", "6623123259")
    API_HASH = environ.get("API_HASH", "AAGrWBfyUP9IFTibaUKaSZZ4EyRbqu2JEcI")
    BOT_TOKEN = environ.get("BOT_TOKEN", "6623123259:AAGrWBfyUP9IFTibaUKaSZZ4EyRbqu2JEcI") 
    BOT_SESSION = environ.get("BOT_SESSION", "bot") 
    DATABASE_URI = environ.get("DATABASE", "mongodb+srv://codewithjai:dYT0VcvoBdeBmCjm@cluster0.q5zm71b.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
    DATABASE_NAME = environ.get("DATABASE_NAME", "forward-bot")
    BOT_OWNER_ID = [int(id) for id in environ.get("BOT_OWNER_ID", '5205621417').split()]

class temp(object): 
    lock = {}
    CANCEL = {}
    forwardings = 0
    BANNED_USERS = []
    IS_FRWD_CHAT = []
    

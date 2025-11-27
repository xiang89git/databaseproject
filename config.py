import os

MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017/DATABASEPROJECT")
SECRET_KEY = os.getenv("SECRET_KEY", "supersecretkey")

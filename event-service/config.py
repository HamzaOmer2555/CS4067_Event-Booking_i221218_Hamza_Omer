import os
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

class Config:
    MONGO_URI = os.getenv("MONGO_URI", "mongodb://admin:adminpassword@event-service-db:27017/event_db")

config = Config()

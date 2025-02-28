import os
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

class Config:
    DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://user:password@user-service-db:5432/user_db")
    JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY", "supersecret")
    JWT_ALGORITHM = "HS256"

config = Config()

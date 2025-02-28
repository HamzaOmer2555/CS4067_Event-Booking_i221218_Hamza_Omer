from fastapi import FastAPI
from database import engine, Base
import routes

# Create database tables
Base.metadata.create_all(bind=engine)

app = FastAPI()

# Include routes
app.include_router(routes.router)

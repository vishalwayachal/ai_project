"""Entry point for running the FastAPI application."""

import uvicorn
from dotenv import load_dotenv
from app.main import app
from app.core.config import Config

# Load environment variables from .env file
load_dotenv()

if __name__ == "__main__":
    uvicorn.run(app, host=Config.HOST, port=Config.PORT)
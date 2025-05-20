"""Configuration module for loading environment variables."""

import os
from dotenv import load_dotenv

# Load environment variables from a .env file
load_dotenv()

class Config:
    """Configuration class to manage application settings.

    This class loads environment variables and provides default values for
    application settings such as the app name, version, host, port, and logging level.
    """
    APP_NAME = os.getenv("APP_NAME", "AI-Modules")
    VERSION = os.getenv("VERSION", "1.0.0")
    HOST = os.getenv("HOST", "0.0.0.0")
    PORT = int(os.getenv("PORT", "8000"))
    ENV = os.getenv("ENV", "dev")
    LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")
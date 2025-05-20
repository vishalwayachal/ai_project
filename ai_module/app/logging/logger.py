"""Logger configuration for the application."""

import logging
import os
from app.core.config import Config
from dotenv import load_dotenv

class LoggerConfig:
    """Logger configuration class.

    This class sets up logging for the application, including file and stream handlers,
    and ensures logs are written to environment-specific files.
    """

# Determine log file path based on environment
env = os.getenv("ENV", "dev")
# Load environment variables from .env file
load_dotenv()

log_file_path = os.getenv("LOG_FILE_PATH", f"/var/log/riavera/{env}/ai-module.log")

# Ensure the log directory exists
os.makedirs(os.path.dirname(log_file_path), exist_ok=True)

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler(log_file_path),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(Config.APP_NAME)
logger.info("Logger initialized with environment-specific file logging.")
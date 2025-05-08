import os

from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()


class Config:
    """
    Dynamic configuration class that reads
    from environment variables on demand.
    """

    @property
    def BOT_TOKEN(self):
        """Get the bot token from environment variables."""
        return os.getenv("BOT_TOKEN")

    @property
    def WHISPER_MODEL(self):
        """
        Get the whisper model from environment variables
        or use the default.
        """
        return os.getenv("WHISPER_MODEL", "small")

    def get_bot_token(self):
        """
        Get the bot token from environment variables.
        """
        return self.BOT_TOKEN

    def get_whisper_model(self):
        """
        Get the whisper model from environment variables
        or use the default.
        """
        return self.WHISPER_MODEL


# Create a module-level instance of the Config class
# This makes config.BOT_TOKEN and config.WHISPER_MODEL work as expected
config = Config()

# For backwards compatibility, also expose at module level
BOT_TOKEN = config.BOT_TOKEN
WHISPER_MODEL = config.WHISPER_MODEL

# Make these attributes available when using "from config import *"
__all__ = ["config", "BOT_TOKEN", "WHISPER_MODEL"]

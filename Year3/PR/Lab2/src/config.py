import os

from dotenv import load_dotenv

load_dotenv()


def get_env_or_raise(key: str) -> str:
    """Get an environment variable or raise an exception."""
    value = os.getenv(key)
    if value is None:
        raise ValueError(f"Environment variable {key} is not set")
    return value


POSTGRES_HOST = get_env_or_raise("POSTGRES_HOST")
POSTGRES_PORT = get_env_or_raise("POSTGRES_PORT")
POSTGRES_USER = get_env_or_raise("POSTGRES_USER")
POSTGRES_PASSWORD = get_env_or_raise("POSTGRES_PASSWORD")
POSTGRES_DB = get_env_or_raise("POSTGRES_DB")
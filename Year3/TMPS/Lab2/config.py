from dotenv import load_dotenv
import os

load_dotenv(dotenv_path=".env")

API_KEY = os.getenv("API_KEY")
URL = os.getenv("URL")
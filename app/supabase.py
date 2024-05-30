import os
from supabase import create_client, Client
from dotenv import load_dotenv


url: str = os.getenv("DB_URL")
key: str = os.getenv("DB_KEY")
supabase: Client = create_client(url, key)
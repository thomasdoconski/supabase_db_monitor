from supabase import create_client, Client
import logging
from config.settings import SUPABASE_URL, SUPABASE_KEY

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

def get_database_size():
    try:
        response = supabase.rpc("get_database_size").execute()
        if response.data:
            return response.data
        else:
            return None
    except Exception as e:
        logging.error(f"Ocorreu um erro ao consultar o Supabase: {e}")
        return None

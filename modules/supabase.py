from supabase import create_client, Client
import logging
from config.settings import SUPABASE_URL, SUPABASE_KEY, MESSAGES

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

def get_database_size():
    try:
        response = supabase.rpc("get_database_size").execute()
        if response.data:
            logging.info(MESSAGES["database_size_retrieved"].format(size=response.data))
            return response.data
        else:
            logging.warning(MESSAGES["database_size_retrieval_failure"])
            return None
    except Exception as e:
        logging.error(MESSAGES["supabase_query_error"].format(error=e))
        return None

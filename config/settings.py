import os
from dotenv import load_dotenv

# Carregar variáveis de ambiente do arquivo .env
load_dotenv()

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")
DISCORD_WEBHOOK_URL = os.getenv("DISCORD_WEBHOOK_URL")
LOG_FILE_PATH = os.path.join(os.path.dirname(__file__), '..', 'logs', 'monitor_log.txt')
PREVIOUS_SIZE_FILE = os.path.join(os.path.dirname(__file__), '..', 'data', 'previous_size.pkl')
import os
import json
from dotenv import load_dotenv

# Carregar variáveis de ambiente do arquivo .env
load_dotenv()

#Supabase related variables
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

#Slack related variable
SLACK_WEBHOOK_URL = os.getenv("SLACK_WEBHOOK_URL")

#Discord related variables
DISCORD_WEBHOOK_URL = os.getenv("DISCORD_WEBHOOK_URL")
DISCORD_WEBHOOK_BOT_CUSTOM_NAME = os.getenv("DISCORD_WEBHOOK_BOT_CUSTOM_NAME")
DISCORD_WEBHOOK_AVATAR_URL = os.getenv("DISCORD_WEBHOOK_AVATAR_URL")

#Custom data store variables (log and previous size)
LOG_FILE_PATH = os.getenv("LOG_FILE_PATH", os.path.join(os.path.dirname(__file__), '..', 'logs', 'monitor_log.txt'))
PREVIOUS_SIZE_FILE = os.getenv("PREVIOUS_SIZE_FILE", os.path.join(os.path.dirname(__file__), '..', 'data', 'previous_size.pkl'))

#Internal configuration variables
LANGUAGE = os.getenv("LANGUAGE", "en-us")
messages_file_path = os.path.join(os.path.dirname(__file__), 'messages', f'{LANGUAGE}.json')
with open(messages_file_path, 'r', encoding='utf-8') as f:
    MESSAGES = json.load(f)
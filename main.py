import logging
from modules.monitor import monitor_supabase
from config.settings import LOG_FILE_PATH

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s', filename=LOG_FILE_PATH, filemode='a', encoding='utf-8')

if __name__ == "__main__":
    monitor_supabase()

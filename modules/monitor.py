import logging
from .discord import send_discord_notification
from .supabase import get_database_size
from .pickle_utils import load_from_pickle, save_to_pickle
from config.settings import PREVIOUS_SIZE_FILE

def monitor_supabase():
    previous_size = load_from_pickle(PREVIOUS_SIZE_FILE)
    database_size = get_database_size()
    if database_size:
        size_str = database_size.strip().upper()
        size_value = float(size_str.split()[0])  # Assumindo que o valor está no formato "XX MB"
        if previous_size is not None and size_value != previous_size:
            change = size_value - previous_size
            message = f"O tamanho do banco de dados mudou de {previous_size} MB para {size_value} MB (variação de {change:.2f} MB). Limite 500MB."
        else:
            message = f"O tamanho atual do banco de dados é: {size_value} MB (limite 500MB)."
        send_discord_notification(message)
        logging.info(message)
        save_to_pickle(PREVIOUS_SIZE_FILE, size_value)
    else:
        logging.warning("Não foi possível obter o tamanho do banco de dados.")

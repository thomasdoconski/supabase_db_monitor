import logging
from .discord import send_discord_notification
from .slack import send_slack_notification
from .supabase import get_database_size
from .pickle_utils import load_from_pickle, save_to_pickle
from config.settings import PREVIOUS_SIZE_FILE, MESSAGES

def monitor_supabase():
    previous_size = load_from_pickle(PREVIOUS_SIZE_FILE)
    database_size = get_database_size()
    if database_size:
        size_str = database_size.strip().upper()
        size_value = float(size_str.split()[0])  # Assumindo que o valor está no formato "XX MB"
        if previous_size is not None and size_value != previous_size:
            change = size_value - previous_size
            message = MESSAGES["database_size_changed"].format(
                previous_size=previous_size, current_size=size_value, change=change)
        else:
            message = MESSAGES["database_size_retrieved"].format(size=size_value)
        send_discord_notification(message)
        send_slack_notification(message)
        logging.info(message)
        save_to_pickle(PREVIOUS_SIZE_FILE, size_value)
    else:
        logging.warning("Não foi possível obter o tamanho do banco de dados.")

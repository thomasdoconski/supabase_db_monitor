import requests
import logging
from config.settings import DISCORD_WEBHOOK_URL

def send_discord_notification(message: str):
    data = {
        "content": message,
    }
    response = requests.post(DISCORD_WEBHOOK_URL, json=data)
    if response.status_code == 204:
        logging.info("Notificação enviada com sucesso ao Discord.")
    else:
        logging.error(f"Falha ao enviar notificação. Código de status: {response.status_code}, Resposta: {response.text}")

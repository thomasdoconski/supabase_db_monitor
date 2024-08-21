import requests
import logging
from config.settings import SLACK_WEBHOOK_URL

def send_slack_notification(message: str):
    if not SLACK_WEBHOOK_URL:
        logging.error("SLACK_WEBHOOK_URL não está configurado.")
        return

    data = {
        "text": message,
    }
    try:
        response = requests.post(SLACK_WEBHOOK_URL, json=data)
        if response.status_code == 200:
            logging.info("Notificação enviada com sucesso ao Slack.")
        else:
            logging.error(f"Falha ao enviar notificação para o Slack. Código de status: {response.status_code}, Resposta: {response.text}")
    except Exception as e:
        logging.error(f"Ocorreu um erro ao enviar notificação para o Slack: {e}")

import requests
import logging
from config.settings import DISCORD_WEBHOOK_URL, DISCORD_WEBHOOK_BOT_CUSTOM_NAME, DISCORD_WEBHOOK_AVATAR_URL, MESSAGES

def send_discord_notification(message: str):
    data = {
        "content": message
    }
    if DISCORD_WEBHOOK_BOT_CUSTOM_NAME:
        data["username"] = DISCORD_WEBHOOK_BOT_CUSTOM_NAME
    if DISCORD_WEBHOOK_AVATAR_URL:
        data["avatar_url"] = DISCORD_WEBHOOK_AVATAR_URL
    
    response = requests.post(DISCORD_WEBHOOK_URL, json=data)
    if response.status_code == 204:
        logging.info(MESSAGES["discord_notification_success"])
    else:
        logging.error(MESSAGES["discord_notification_failure"].format(
            status_code=response.status_code, response_text=response.text))

import requests

BOT_TOKEN = "توکن_ربات"
CHAT_ID = "چت_آیدی"

def send():
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    
    data = {
        "chat_id": CHAT_ID,
        "text": "✅ GitHub scanner test message"
    }

    requests.post(url, data=data)

send()

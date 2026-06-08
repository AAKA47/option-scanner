import requests

BOT_TOKEN = "8727264897:AAHKRXC4znJi3CG1j8yKZLn9z2jGov8F-Pg"
CHAT_ID = "101936503"

def send():
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    
    data = {
        "chat_id": CHAT_ID,
        "text": "✅ GitHub scanner test message"
    }

    requests.post(url, data=data)

send()

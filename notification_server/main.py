import requests
from flask import Flask
from flask import request

from NotificationMessage import NotificationMessage

app = Flask(__name__)

bot_token = '6060431646:AAG3GfZz6sfCjUfQrSwPmE6hFozvElZ4Fm0'
channel_id = -1001928906185


@app.route('/send-notification', methods=['POST'])
def send_notification():
    body = request.get_json()
    msg = NotificationMessage(body.get("_check_name"), body.get("_level"), body.get("_message"))
    result = send_message(f"{msg.name}: {msg.level.upper()}\n{msg.message}")
    return result


def send_message(msg):
    url_req = f"https://api.telegram.org/bot{bot_token}/sendMessage?chat_id={channel_id}&text={msg}"
    results = requests.get(url_req)
    return results.json()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)

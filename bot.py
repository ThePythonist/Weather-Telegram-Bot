from flask import Flask, request
import telepot
import urllib3
from key import token
from weather import *

proxy_url = "http://proxy.server:3128"
telepot.api._pools = {
    'default': urllib3.ProxyManager(proxy_url=proxy_url, num_pools=3, maxsize=10, retries=False, timeout=30),
}
telepot.api._onetime_pool_spec = (
    urllib3.ProxyManager, dict(proxy_url=proxy_url, num_pools=1, maxsize=1, retries=False, timeout=30))

secret = "BOT"
bot = telepot.Bot(token)
bot.setWebhook("https://thepythonist2.pythonanywhere.com/{}".format(secret), max_connections=1)

app = Flask(__name__)


def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    print(content_type, chat_type, chat_id)

    if content_type == 'text':
        if msg["text"] == "/start":
            bot.sendMessage(chat_id, "Hey there! Welcome to weather bot. Send me a city name :")
        else:
            name = get_weather_data(msg["text"])["name"]
            temp = get_weather_data(msg["text"])["temp"]
            hum = get_weather_data(msg["text"])["hum"]
            date = get_weather_data(msg["text"])["date"]
            reply = f"""
City : {name}
Date : {date}
Temperature : {temp}
Humidity : {hum}
"""
            bot.sendMessage(chat_id,reply )
    else:
        bot.sendMessage(chat_id, "Send me text only.")


@app.route('/{}'.format(secret), methods=["POST"])
def telegram_webhook():
    update = request.get_json()
    if "message" in update:
        handle(update["message"])
    return "OK"

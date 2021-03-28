import telebot
import requests
from flask import Flask, request, make_response, jsonify
import json
from geopy.geocoders import Nominatim
import os
from datetime import datetime

app = Flask(__name__)
API_KEY = 'e81a53eda410c7faee40fb24a7e62de8'
bot=telebot.TeleBot('1780813668:AAE14WC0tM2Hc64husBSR0ebUR6St2NPgtU')
#
def results():
    req = request.get_json(force=True)

    action = req.get('queryResult').get('action')

    result = req.get("queryResult")
    parameters = result.get("parameters")

    if parameters.get('location').get('city'):
        geolocator = Nominatim(user_agent='weather-bot')
        location = geolocator.geocode(parameters.get('location').get('city'))
        lat = location.latitude
        long = location.longitude
        weather_req = requests.get(
            'https://api.openweathermap.org/data/2.5/onecall?lat={}&lon={}&appid={}'.format(lat, long, 'e81a53eda410c7faee40fb24a7e62de8'))
        current_weather = json.loads(weather_req.text)['current']
        temp = round(current_weather['temp'] - 273.15)
        feels_like = round(current_weather['feels_like'] - 273.15)
        clouds = current_weather['clouds']
        wind_speed = current_weather['wind_speed']

    return {
        'fulfillmentText': 'Сейчас температура воздуха - {} градусов, ощущается как {} градусов, облачность - {}%, скорость ветра - {}м/с'.format(
            str(temp), str(feels_like), str(clouds), str(wind_speed))}
#
@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Нахуй иди')

@bot.message_handler(commands=['weather'])
def start_message(message):
    bot.send_message(message.chat.id, results())

@bot.message_handler(content_types=["text"])
def text(message):
    if message.text == 'Сам иди':
        bot.send_message(message.chat.id, 'Мать жива?')
    if message.text == 'Сам иди':
        bot.send_message(message.chat.id, 'Мать жива?')


bot.polling()
#res = requests.get(
#    'https://'
#)
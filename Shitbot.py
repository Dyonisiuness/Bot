import telebot
import pyowm
import requests
from flask import Flask, request, make_response, jsonify
import json
from geopy.geocoders import Nominatim
import os
from datetime import datetime

app = Flask(__name__)
API_KEY = 'e81a53eda410c7faee40fb24a7e62de8'
bot = telebot.TeleBot('1780813668:AAE14WC0tM2Hc64husBSR0ebUR6St2NPgtU')
@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Нахуй иди')

# @bot.message_handler(commands=['weather'])
# def start_message(message):
#    bot.send_message(message.chat.id, results())


@bot.message_handler(content_types=["text"])
def text(message):
    if message.text == 'Сам иди':
        bot.send_message(message.chat.id, 'Мать жива?')
    if message.text == 'Пароль - BotIsDegenerate':
        bot.send_message(message.chat.id, 'Бот согласен')


bot.polling(none_stop=True)
# res = requests.get(
#    'https://')
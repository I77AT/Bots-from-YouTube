import telebot
import requests
import json

bot = telebot.TeleBot('')
API = ''

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id,'Напиши название города')

@bot.message_handler(content_types=['text'])
def get_weather(message):
    city = message.text.strip().lower()
    res = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API}&units=metric')
    if res.status_code== 200:
        data = json.loads(res.text)
        temp = data["main"]["temp"]
        emoji = '☀️' if temp > 5.0 else '🌤'
        bot.reply_to(message,f'Сейчас погода {temp}{emoji}')

    else:
        bot.reply_to(message, 'Город неверно указан')


bot.polling(non_stop=True)
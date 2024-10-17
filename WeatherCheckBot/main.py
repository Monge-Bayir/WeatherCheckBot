import telebot
import requests
import json

bot = telebot.TeleBot('7687491251:AAFiX5zHXgZQSF3c80FM7fmWOMbzOEw3oxQ')
API = 'ed4f4cb4aa49bf4ca25bdd1110865fd0'


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Привет, рад тебя видеть, мой друг! Напиши название своего города')


@bot.message_handler(content_types=['text'])
def get_weather(message):
    city = message.text.strip().lower()
    res = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API}&units=metric')

    if res.status_code == 200:
        data = json.loads(res.text)
        temp = data["main"]["temp"]
        bot.reply_to(message, f'Сейчас погода: {temp}')

        image = 'photo/sunny.png' if temp > 5.0 else 'photo/cold.png'
        file = open(image, 'rb')
        bot.send_photo(message.chat.id, file)

    else:
        bot.reply_to(message, f'Город указан неверно')


bot.polling(non_stop=True)
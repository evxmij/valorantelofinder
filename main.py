import telebot
import requests
from settings import TOKEN, valorant_region


bot = telebot.TeleBot(TOKEN)

user_data = {}

@bot.message_handler(commands=['start'])
def start(message):
    user_data[message.chat.id] = {'step': 0}
    bot.send_message(message.chat.id, "Привет!\nТут ты можешь узнать ранг по RiotID\nОтправь мне Riot ID(без #)\nНапример riot id valo#rant\nСначала отправь мне valo, а потом rant:)")

@bot.message_handler(func=lambda message: user_data.get(message.chat.id, {}).get('step') == 0)
def riot_id(message):
    chat_id = message.chat.id
    user_data[chat_id]['riot_id'] = message.text
    user_data[chat_id]['step'] = 1
    bot.send_message(chat_id, "Теперь введите Riot Tag")

@bot.message_handler(func=lambda message: user_data.get(message.chat.id, {}).get('step') == 1)
def riot_tag(message):
    chat_id = message.chat.id
    user_data[chat_id]['riot_tag'] = message.text

    riot_id = user_data[chat_id]['riot_id']
    riot_tag = user_data[chat_id]['riot_tag']
    link = f'https://api.kyroskoh.xyz/valorant/v1/mmr/{valorant_region}/{riot_id}/{riot_tag}'

    response = requests.get(link)

    bot.send_message(chat_id, f"Узнаю ваш ранг:\n\nРезультат работы:\n{response.text}")
    user_data[chat_id]['step'] = 0

bot.polling()

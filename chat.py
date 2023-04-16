import os
import json
import telebot

os.system('clear')


# objetivo: este chat se va a correr en otra
# terminal a la del server, y en esta se van
# a ver los mensajes mandados desde el server


# Open the JSON file and read its contents
with open('info.json', 'r') as f:
    data = f.read()
# read the file content as a dic
info = json.loads(data)

name = info['NAME']
# Enter your Telegram bot token here
bot_token = info['TOKEN']
# and the chat id
chat = info['CHAT']
# and create the bot with the token
bot = telebot.TeleBot(bot_token)

# Define the chat ID of the recipient
chat_id = chat


while True:
	# Define the message text
	message_text = input('bchat $ ')

	# Send the message to the recipient
	bot.send_message(chat_id, message_text)
	os.system(f'echo "[{name}]: {message_text} \n" >> /dev/ttys001')


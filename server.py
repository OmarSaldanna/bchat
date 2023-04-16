# objetivo: que se corra en el background el
# servidor para recibir mensajes y que los 
# mensajes se manden a la terminal actual


# The Settings
import os
import json
import telebot
# clear screen and a message
os.system('clear')
print("Welcome To BChat :3 \n")
# Open the JSON file and read its contents
with open('info.json', 'r') as f:
    data = f.read()
# read the file content as a dic
info = json.loads(data)
# Enter your Telegram bot token here
bot_token = info['TOKEN']
# and the chat id
chat = info['CHAT']

# The Bot

# and create the bot with the token
bot = telebot.TeleBot(bot_token)


# function to recieve messages
# function to handle the /m command
# /m message
@bot.message_handler(commands=['m'])
def handle_m_command(message):
    # Get the text after the command name
    command_text = message.text.split(' ',1)[1]
    # Get the author of the message
    author = message.from_user.username
    # print the message
    print(f"[{author}]: {command_text} \n")


# start the bot
bot.infinity_polling()



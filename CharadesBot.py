#This is the code for CharadesBot @Charades_gameBot
import telebot
import time
import requests
import json
import random
from telebot import types

#Replace bot_token with actual token
bot = telebot.TeleBot(token=bot_token)

#Another possible api:
#response = requests.get("https://random-word-api.herokuapp.com/word?number=10")
import datamuse
api = datamuse.Datamuse()
api.words()

def jprint(obj):
    # create a formatted string of the Python JSON object
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)

response = requests.get("https://api.datamuse.com/words?topics=animals&max=1000")
jprint(response.json())
given_word = response.json()

word = []
for w in given_word:
    gw = w['word']
    word.append(gw)

print(word)

#setting up the gameBot
game_score = 0

@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = types.ReplyKeyboardMarkup(one_time_keyboard = True)
    itembtn1 = types.KeyboardButton('1 min')
    itembtn2 = types.KeyboardButton('2 mins')
    itembtn3 = types.KeyboardButton('3 mins')
    itembtn4 = types.KeyboardButton('5 mins')
    markup.row(itembtn1, itembtn2)
    markup.row(itembtn3, itembtn4)
    bot.send_message(message.chat.id, "Welcome to CharadesBot! Please choose the time duration for one game. ", reply_markup=markup)

@bot.message_handler(func=lambda message: message.text == '1 min')
def command_text_time(message):
    bot.send_message(message.chat.id, "Time duration: 1 min. Here is your word!")
    markup = types.ReplyKeyboardMarkup()
    itembtnP = types.KeyboardButton('Pass')
    itembtnS = types.KeyboardButton('Succeed')
    markup.row(itembtnP, itembtnS)
    y = random.randint(1,999)
    bot.send_message(message.chat.id, str(word[y]), reply_markup=markup)
    time.sleep(60)
    global game_score
    bot.send_message(message.chat.id, 'Time is up! You scored: ' + str(game_score))
    game_score = 0

@bot.message_handler(func=lambda message: message.text == '2 mins')
def command_text_time(message):
    bot.send_message(message.chat.id, "Time duration: 2 mins. Here is your word!")
    markup = types.ReplyKeyboardMarkup()
    itembtnP = types.KeyboardButton('Pass')
    itembtnS = types.KeyboardButton('Succeed')
    markup.row(itembtnP, itembtnS)
    y = random.randint(1,999)
    bot.send_message(message.chat.id, str(word[y]), reply_markup=markup)
    time.sleep(120)
    global game_score
    bot.send_message(message.chat.id, 'Time is up! You scored: ' + str(game_score))
    game_score = 0

@bot.message_handler(func=lambda message: message.text == '3 mins')
def command_text_time(message):
    bot.send_message(message.chat.id, "Time duration: 3 mins. Here is your word!")
    markup = types.ReplyKeyboardMarkup()
    itembtnP = types.KeyboardButton('Pass')
    itembtnS = types.KeyboardButton('Succeed')
    markup.row(itembtnP, itembtnS)
    y = random.randint(1,999)
    bot.send_message(message.chat.id, str(word[y]), reply_markup=markup)
    time.sleep(180)
    global game_score
    bot.send_message(message.chat.id, 'Time is up! You scored: ' + str(game_score))
    game_score = 0

@bot.message_handler(func=lambda message: message.text == '5 mins')
def command_text_time(message):
    bot.send_message(message.chat.id, "Time duration: 5 mins. Here is your word!")
    markup = types.ReplyKeyboardMarkup()
    itembtnP = types.KeyboardButton('Pass')
    itembtnS = types.KeyboardButton('Succeed')
    markup.row(itembtnP, itembtnS)
    y = random.randint(1,999)
    bot.send_message(message.chat.id, str(word[y]), reply_markup=markup)
    time.sleep(300)
    global game_score
    bot.send_message(message.chat.id, 'Time is up! You scored: ' + str(game_score))
    game_score = 0

@bot.message_handler(func=lambda message: message.text == "Succeed")
def command_text_succeed(message):
    global game_score
    game_score += 1
    y = random.randint(1,999)
    bot.send_message(message.chat.id, str(word[y]))

@bot.message_handler(func=lambda message: message.text == "Pass")
def command_text_pass(message):
    y = random.randint(1,999)
    bot.send_message(message.chat.id, str(word[y]))

@bot.message_handler(commands=['help'])
def send_help(message):
    bot.reply_to(message, 'To start the game, send /start.')

@bot.message_handler(commands=['quit'])
def send_help(message):
    global game_score
    bot.reply_to(message, 'You have quit the game. Your score is: ' + str(game_score))
    game_score = 0

bot.polling(none_stop = True)

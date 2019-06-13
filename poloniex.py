import telebot
from telebot import types, apihelper
import requests
import time
import misc

bot = telebot.TeleBot(misc.token)
apihelper.proxy = {
  'https':'socks5://165.227.20.194:9050'}

markup = types.ReplyKeyboardMarkup(row_width=3)
markup.row('efir', 'bitcoin', 'help')

markup1 = types.ReplyKeyboardMarkup(row_width=3)
markup1.row('efir')
markup2 = types.ReplyKeyboardMarkup(row_width=3)
markup2.row('bitcoin')

@bot.message_handler(commands=['efir'])
def send_welcome(message):
    efir =requests.get("https://poloniex.com/public?command=returnTicker")
    time.sleep(2)
    print(efir.json()['USDT_ETH']['last'])
    bot.send_message(message.chat.id, str (efir.json()['USDT_ETH']['last']))

@bot.message_handler(commands=['bitcoin'])
def send_welcome(message):
    bitcoin = requests.get("https://poloniex.com/public?command=returnTicker")
    time.sleep(2)
    print(bitcoin.json()['USDT_BTC']['last'])
    bot.send_message(message.chat.id, str (efir.json()['USDT_BTC']['last']))

@bot.message_handler(commands=['help'])
def send_welcome(message):
    bot.send_message(message.chat.id, "Если хочешь узнать курс к доллару - выбери монету", reply_markup=markup)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, "Выбери монету", reply_markup=markup)

if __name__ == "__main__":
    bot.polling(none_stop= True)

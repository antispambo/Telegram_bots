import telebot
from telebot import types

bot = telebot.TeleBot("token_from_bot_father")

@bot.message_handler(commands=["start"])
def start_message(message):
    bot.send_message(message.chat.id, "Welcome")

@bot.message_handler(commands=["link"])
def send_link(message):
    keyboard = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="Go to Yandex", url="https://ya.ru")
    keyboard.add(url_button)
    bot.send_message(message.chat.id, "Open yandex.", reply_markup=keyboard)

@bot.message_handler(commands=["help"])
def help(message):
    bot.send_message(message.chat.id, "/start \n /link")

if __name__ == "__main__":
    bot.infinity_polling()

import telebot
from telebot import types

bot = telebot.TeleBot("bot_token")

@bot.message_handler(commands=["start"])
def start_message(message):
    bot.send_message(message.chat.id, "Привет")

@bot.message_handler(commands=["link"])
def send_link(message):
    keyboard = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="Перейти на Яндекс", url="https://ya.ru")
    keyboard.add(url_button)
    bot.send_message(message.chat.id, "Нажми на кнопку и перейди в поисковик.", reply_markup=keyboard)

@bot.message_handler(commands=["help"])
def help(message):
    bot.send_message(message.chat.id, "/start \n /link")

if __name__ == "__main__":
    bot.infinity_polling()
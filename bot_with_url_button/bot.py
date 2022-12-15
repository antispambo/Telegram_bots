
import telebot
from telebot import types
token = "bot-toket"
bot = telebot.TeleBot(token)

@bot.message_handler(commands=['link'])
def repeat_all_messages(message): # Название функции не играет никакой роли
    keyboard = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="Перейти на Яндекс", url="https://ya.ru")
    keyboard.add(url_button)
    bot.send_message(message.chat.id, "Привет! Нажми на кнопку и перейди в поисковик.", reply_markup=keyboard)

if __name__ == '__main__':
     bot.infinity_polling()
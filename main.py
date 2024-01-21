import telebot
from telebot import types
# import webbrowser
# # import os

bot = telebot.TeleBot('6678325818:AAH5FXcp3wo52XrXFtg28Sd9NJU01aqWM24')


@bot.message_handler(content_types=['photo'])
def get_photo(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('Go to website', url='https://google.com'))
    bot.reply_to(message, 'This image is wonderful', reply_markup=markup)

# @bot.message_handler(commands=['site', 'website'])
# def site(message):
#     webbrowser.open('https://youtube.com')


# @bot.message_handler(commands=['start', 'main', 'hello'])
# def main(message):
#     bot.send_message(message.chat.id, f'Hello, {message.from_user.first_name}')


# @bot.message_handler(commands=['help'])
# def main(message):
#     bot.send_message(message.chat.id, '<strong><em>Help info</em></strong>', parse_mode="html")


# @bot.message_handler()
# def info(message):
#     if message.text.lower() == 'hello':
#         bot.send_message(message.chat.id, f'Hello, {message.from_user.first_name}')
#     elif message.text.lower() == 'id':
#         bot.reply_to(message, f'ID: {message.from_user.id}')


# # try:
# #     os.system('python main.py')
# # except RuntimeError:
# #     os.system('python main.py')



bot.polling(none_stop=True)
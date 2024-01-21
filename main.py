import telebot
from telebot import types
# import webbrowser


bot = telebot.TeleBot('6678325818:AAHyF9QMaKjZiYX2fGMgSW2tapKWeVm-gwE')


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup()
    btn1 = types.KeyboardButton('Go to website')
    btn2 = types.KeyboardButton('Delete the photo')
    btn3 = types.KeyboardButton('Change text')
    markup.row(btn1)
    markup.row(btn2, btn3)
    file = open('./photo.jpg', 'rb')
    # bot.send_photo(message.chat.id, file, reply_markup=markup)
    # bot.send_audio(message.chat.id, file, reply_markup=markup)
    # bot.send_video(message.chat.id, file, reply_markup=markup)
    # bot.send_animation(message.chat.id, file, reply_markup=markup)
    # bot.send_message(message.chat.id, 'Hello', reply_markup=markup)
    bot.register_next_step_handler(message, on_click1)


def on_click1(message):
    if message.text == 'Go to website':
        bot.send_message(message.chat.id, 'Website is open')
    bot.register_next_step_handler(message, on_click2)

def on_click2(message):
    if message.text == 'Delete the photo':
        bot.send_message(message.chat.id, 'The photo deleted')
    bot.register_next_step_handler(message, on_click3)

def on_click3(message):
    if message.text == 'Change text':
        bot.send_message(message.chat.id, 'Text changed')


@bot.message_handler(content_types=['photo'])
def get_photo(message):
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton('Go to website', url='https://google.com')
    btn2 = types.InlineKeyboardButton('Delete the photo', callback_data='delete')
    btn3 = types.InlineKeyboardButton('Change text', callback_data='edit')
    markup.row(btn1)
    markup.row(btn2, btn3)
    bot.reply_to(message, 'This image is wonderful', reply_markup=markup)


@bot.callback_query_handler(func=lambda callback: True)
def callback_message(callback):
    if callback.data == 'delete':
        bot.delete_message(callback.message.chat.id, callback.message.message_id-1)
    elif callback.data == 'edit':
        bot.edit_message_text('Edit text', callback.message.chat.id, callback.message.message_id)

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



bot.infinity_polling()
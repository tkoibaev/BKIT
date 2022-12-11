import telebot
import googletrans
from telebot import types
from googletrans import Translator


bot=telebot.TeleBot('5789470518:AAEr1g_ILH9DGBR5byzwToZhp20FP14AfxI')

@bot.message_handler(commands=['start'])
def button(message):
    markup = types.InlineKeyboardMarkup(row_width=2)
    item1 = types.InlineKeyboardButton('Все хорошо',callback_data='good')
    item2 = types.InlineKeyboardButton('Как-то не очень',callback_data='bad')
    markup.add(item1,item2)

    bot.send_message(message.chat.id, "Привет! Как дела?", reply_markup=markup)


@bot.callback_query_handler(func=lambda call:True)
def callback(call):
    if call.message:
        if call.data == 'good':
            #photo=open('gi.jpg','rb')
            bot.send_message(call.message.chat.id,"Это же прекрасно!")
        elif call.data == 'bad':
            #photo = open('Messi.jpg','rb')
            bot.send_message(call.message.chat.id,"Не грусти, все будет хорошо)")

@bot.message_handler(commands=['help'])
def button(message):
    markupu = types.ReplyKeyboardMarkup(resize_keyboard=True,row_width=1)
    it1 = types.KeyboardButton('Ништяк 1')
    it2 = types.KeyboardButton('Ништяк 2')
    it3 = types.KeyboardButton('Ништяк 3')

    markupu.add(it1, it2, it3)

    bot.send_message(message.chat.id, "Посмотри под поле ввода", reply_markup=markupu)

@bot.message_handler(content_types='text')
def send_vid(message):
    if message.text == 'Ништяк 1':
        video=open('1.mp4','rb')
        bot.send_video(message.chat.id,video)
    elif message.text == 'Ништяк 2':
        video=open('2.mp4','rb')
        print('debug2')
        bot.send_video(message.chat.id,video)
    elif message.text == 'Ништяк 3':
        video=open('3.mp4','rb')
        bot.send_video(message.chat.id,video)


bot.polling(none_stop=True)
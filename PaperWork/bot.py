import telebot
from house import *
from room import *

token = "6770626969:AAFpMdob6fY824wm3uZVaqP4lEFwoYL52Jw"
bot = telebot.TeleBot(token)

HELP = """
/info - вывести список доступных действий
/house - расчтать по данным мощность котла и оборот всего объёма теплоносителя в один час
/room - расчитать по данным количество секций радиатора в комнате
"""

@bot.message_handler(commands = ["info", "start"])
def info(message):
    bot.send_message(message.chat.id, HELP)

@bot.message_handler(commands = ["house"])
def house(message):
    bot.send_photo(message.chat.id, "https://frankfurt.apollo.olxcdn.com/v1/files/mm589vydlv22-KZ/image;s=1000x700")
    bot.send_message(message.chat.id, "Введите длину, ширину и высоту дома через пробел:")
    House_(bot)

@bot.message_handler(commands=["room"])
def room(message):
    bot.send_photo(message.chat.id, "https://static.tildacdn.com/tild6366-3234-4863-b135-383035613232/Group_823.jpg")
    text = "Выберите остекление:"
    win_mat1 = ["Обычное", "Двойное", "Тройное"]
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(types.InlineKeyboardButton(win_mat1[0], callback_data='1'))
    markup.add(types.InlineKeyboardButton(win_mat1[1], callback_data='2'))
    markup.add(types.InlineKeyboardButton(win_mat1[2], callback_data='3'))
    bot.send_message(message.chat.id, text, reply_markup=markup)
    Room_(bot)

bot.polling(none_stop=True)
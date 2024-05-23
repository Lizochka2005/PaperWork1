import math
from telebot import types
from oop import *
from check import *

a = Room()
b = House()
c = House_multip()

def Room_(bot):
    @bot.callback_query_handler(func=lambda c: c.data in ['1', '2', '3'])
    def window_mat(c):
        if c.data == "1":
            a.k1 = 1.27
            print(1.27)
        elif c.data == "2":
            a.k1 = 1
            print(1)
        else:
            a.k1 = 0.85
            print(0.85)
        bot.send_photo(c.message.chat.id, "https://avatars.mds.yandex.net/i?id=65dc7d5d1fafcc47964a76afbabc554c_l-10517487-images-thumbs&n=33&w=1138&h=1080&q=60")
        text = "Выберите теплоизоляцию стен:"
        isol = ["Низкая", "Средняя", "Высокая"]
        markup = types.InlineKeyboardMarkup(row_width=2)
        markup.add(types.InlineKeyboardButton(isol[0], callback_data='l'))
        markup.add(types.InlineKeyboardButton(isol[1], callback_data='s'))
        markup.add(types.InlineKeyboardButton(isol[2], callback_data='h'))
        bot.send_message(c.message.chat.id, text, reply_markup=markup)

    @bot.callback_query_handler(func=lambda c: c.data in ['l', 's', 'h'])
    def isolation(c):
        if c.data == "l":
            a.k2 = 1.27
            print(1.27)
        elif c.data == "s":
            a.k2 = 1
            print(1)
        else:
            a.k2 = 0.85
            print(0.85)
        bot.send_photo(c.message.chat.id, "https://sun9-34.userapi.com/impg/mABu9lmAwHlSM5btrQttHb-pMhsbRT8_EiwDCw/aIuU2gk4R4c.jpg?size=882x1080&quality=96&sign=823f7c9754b3e2d8bda340aa540a57e1&c_uniq_tag=vRNT0HnSPz5i9rCPxbXXvrnJLHuZ33x5NB5pvmYGTaQ&type=album")
        bot.send_message(c.message.chat.id, "Введите количество окон в комнате, их длину, ширину через пробел:")
        bot.register_next_step_handler(c.message, window)

    def window(message):
        if is_nvalue(message.text, 3):
            bot.send_message(message.chat.id, 'К сожалению вы неправильно ввели данные:( Попробуйте снова!')
            bot.send_photo(message.chat.id, "https://sun9-34.userapi.com/impg/mABu9lmAwHlSM5btrQttHb-pMhsbRT8_EiwDCw/aIuU2gk4R4c.jpg?size=882x1080&quality=96&sign=823f7c9754b3e2d8bda340aa540a57e1&c_uniq_tag=vRNT0HnSPz5i9rCPxbXXvrnJLHuZ33x5NB5pvmYGTaQ&type=album")
            bot.send_message(message.chat.id, "Введите количество окон в комнате, их длину, ширину через пробел:")
            bot.register_next_step_handler(message, window)
        else:
            lw = message.text.split()
            b.count_w = int(lw[0])
            b.len_w = float(lw[1])
            b.wide_w = float(lw[2])
            b.s_win = b.count_w * c.Square(b.len_w, b.wide_w)
            bot.send_message(message.chat.id, 'Суммарная площадь окон = {}'.format(b.s_win))
            bot.send_photo(message.chat.id, "https://avatars.mds.yandex.net/i?id=93454bc610a29c6eb376347ff8b91967_l-5221577-images-thumbs&n=13")
            bot.send_message(message.chat.id, "Введите длину, ширину комнаты через пробел:")
            bot.register_next_step_handler(message, room)

    def room(message):
        if is_nvalue(message.text, 2):
            bot.send_message(message.chat.id, 'К сожалению вы неправильно ввели данные:( Попробуйте снова!')
            bot.send_photo(message.chat.id, "https://avatars.mds.yandex.net/i?id=93454bc610a29c6eb376347ff8b91967_l-5221577-images-thumbs&n=13")
            bot.send_message(message.chat.id, "Введите длину, ширину комнаты через пробел:")
            bot.register_next_step_handler(message, room)
        else:
            lw = message.text.split()
            a.room_len = float(lw[0])
            a.room_wide = float(lw[1])
            a.room_s = c.Square(a.room_len, a.room_wide)
            bot.send_message(message.chat.id, 'Площадь комнаты = {}'.format(a.room_s))
            percent = (b.s_win/a.room_s)*100
            if percent > 50:
                a.k3 = 1.2
            elif percent > 40:
                a.k3 = 1.1
            elif percent > 30:
                a.k3 = 1
            elif percent > 20:
                a.k3 = 0.9
            elif percent > 10:
                a.k3 = 0.8
            else:
                a.k3 = 0.7
            bot.send_photo(message.chat.id, "https://avatars.mds.yandex.net/i?id=d04799fc9e780b8cef6e5528c71b1e1e_l-6295814-images-thumbs&n=13")
            text = "Выберите средний показатель температуры зимой:"
            temp = ["-35","-30", "-25", "-20", "-15", "-10"]
            markup = types.InlineKeyboardMarkup(row_width=2)
            markup.add(types.InlineKeyboardButton(temp[0], callback_data='35'))
            markup.add(types.InlineKeyboardButton(temp[1], callback_data='30'))
            markup.add(types.InlineKeyboardButton(temp[2], callback_data='25'))
            markup.add(types.InlineKeyboardButton(temp[3], callback_data='20'))
            markup.add(types.InlineKeyboardButton(temp[4], callback_data='15'))
            markup.add(types.InlineKeyboardButton(temp[5], callback_data='10'))
            bot.send_message(message.chat.id, text, reply_markup=markup)

    @bot.callback_query_handler(func=lambda c: c.data in ['35', '30', '25', '20', '15', '10'])
    def tempreture(c):
        if c.data == "35":
            a.k4 = 1.5
            print(1.5)
        elif c.data == "30":
            a.k4 = 1.4
            print(1.4)
        elif c.data == "25":
            a.k4 = 1.3
            print(1.3)
        elif c.data == "20":
            a.k4 = 1.1
            print(1.1)
        elif c.data == "15":
            a.k4 = 0.9
            print(0.9)
        else:
            a.k4 = 0.7
            print(0.7)
        bot.send_photo(c.message.chat.id, "https://cch-rc.com/wp-content/uploads/2018/05/wall.jpg")
        text = "Выберите количество стен, выходящих наружу:"
        count = ["1", "2", "3", "4"]
        markup = types.InlineKeyboardMarkup(row_width=2)
        markup.add(types.InlineKeyboardButton(count[0], callback_data='1c'))
        markup.add(types.InlineKeyboardButton(count[1], callback_data='2c'))
        markup.add(types.InlineKeyboardButton(count[2], callback_data='3c'))
        markup.add(types.InlineKeyboardButton(count[3], callback_data='4c'))
        bot.send_message(c.message.chat.id, text, reply_markup=markup)

    @bot.callback_query_handler(func=lambda c: c.data in ['1c', '2c', '3c', '4c'])
    def wall_outside(c):
        if c.data == "1c":
            a.k5 = 1.1
            print(1.1)
        elif c.data == "2c":
            a.k5 = 1.2
            print(1.2)
        elif c.data == "3c":
            a.k5 = 1.3
            print(1.3)
        else:
            a.k5 = 1.4
            print(1.4)
        a.k6 = 0.9
        bot.send_photo(c.message.chat.id, "https://avatars.mds.yandex.net/i?id=30e445b1f51adb9a1c98d7f110e615e0_l-5273210-images-thumbs&n=33&w=1080&h=1080&q=60")
        text = "Выберите высоту потолка:"
        high = ["2.5", "3", "3.5", "4", "4.5", "5"]
        markup = types.InlineKeyboardMarkup(row_width=2)
        markup.add(types.InlineKeyboardButton(high[0], callback_data='2.5h'))
        markup.add(types.InlineKeyboardButton(high[1], callback_data='3h'))
        markup.add(types.InlineKeyboardButton(high[2], callback_data='3.5h'))
        markup.add(types.InlineKeyboardButton(high[3], callback_data='4h'))
        markup.add(types.InlineKeyboardButton(high[4], callback_data='4.5h'))
        markup.add(types.InlineKeyboardButton(high[5], callback_data='5h'))
        bot.send_message(c.message.chat.id, text, reply_markup=markup)

    @bot.callback_query_handler(func=lambda c: c.data in ['2.5h', '3h', '3.5h', '4h', '4.5h', '5h'])
    def hight(c):
        if c.data == "2.5h":
            a.k7 = 1
            print(1)
        elif c.data == "3h":
            a.k7 = 1.05
            print(1.05)
        elif c.data == "3.5h":
            a.k7 = 1.1
            print(1.1)
        elif c.data == "4h":
            a.k7 = 1.15
            print(1.15)
        elif c.data == "4.5h":
            a.k7 = 1.2
            print(1.2)
        else:
            a.k7 = 1.25
            print(1.25)
        bot.send_photo(c.message.chat.id, "https://thermshop.ru/netcat_files/200/271/1440435918.735_10.jpg")
        text = "Выберите тип радиатора:"
        rad = ["Чугунный", "Алюминиевый", "Биметаллический"]
        markup = types.InlineKeyboardMarkup(row_width=2)
        markup.add(types.InlineKeyboardButton(rad[0], callback_data='Ch'))
        markup.add(types.InlineKeyboardButton(rad[1], callback_data='Al'))
        markup.add(types.InlineKeyboardButton(rad[2], callback_data='B'))
        bot.send_message(c.message.chat.id, text, reply_markup=markup)

    @bot.callback_query_handler(func=lambda c: c.data in ['Al', 'Ch', 'B'])
    def radiator(c):
        if c.data == "Ch":
            a.C = 150
            print(150)
        elif c.data == "Al":
            a.C = 190
            print(190)
        else:
            a.C = 200
            print(200)
        a.N = math.ceil((100 * a.k1 * a.k2 * a.k3 * a.k4 * a.k5 * a.k6 * a.k7 * a.room_s)/a.C)
        bot.send_message(c.message.chat.id, 'Количество секций радиатора, необходимое для отопления комнаты = {}'.format(a.N))

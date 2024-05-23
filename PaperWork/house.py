import math
from telebot import types
from oop import *
from check import *

b = House()
a = House_multip()

def House_(bot):
    @bot.message_handler(content_types=['text'])
    def house(message):
        if is_nvalue(message.text,3):
            bot.send_message(message.chat.id, 'К сожалению вы неправильно ввели данные:( Попробуйте снова!')
            bot.send_photo(message.chat.id, "https://frankfurt.apollo.olxcdn.com/v1/files/mm589vydlv22-KZ/image;s=1000x700")
            bot.send_message(message.chat.id, "Введите длину, ширину и высоту дома через пробел:")
            bot.register_next_step_handler(message, house)
        else:
            lwh = message.text.split()
            b.len = float(lwh[0])
            b.wide = float(lwh[1])
            b.high = float(lwh[2])
            b.s = a.Square(b.len,b.wide)
            bot.send_message(message.chat.id, 'Площадь дома = {}'.format(b.s))
            b.v = a.Volume(b.high, b.s)
            bot.send_message(message.chat.id, 'Объём дома = {}'.format(b.v))
            bot.send_photo(message.chat.id, "https://beton-lebyazhe.ru/assets/template/images/STROITELSTVO/stroitelstvo-fundamenta.jpg")
            bot.send_message(message.chat.id, "Введите толщину фундамента:")
            bot.register_next_step_handler(message, floor)

    def floor(message):
        if is_nvalue(message.text, 1):
            bot.send_message(message.chat.id, 'К сожалению вы неправильно ввели данные:( Попробуйте снова!')
            bot.send_photo(message.chat.id, "https://beton-lebyazhe.ru/assets/template/images/STROITELSTVO/stroitelstvo-fundamenta.jpg")
            bot.send_message(message.chat.id, "Введите толщину фундамента:")
            bot.register_next_step_handler(message, floor)
        else:
            b.thick_floor = float(message.text)
            text = "Выберите материал фундамента:"
            floor_mat1 = ["Бетон", "Железобетон"]
            markup = types.InlineKeyboardMarkup(row_width=2)
            markup.add(types.InlineKeyboardButton(floor_mat1[0], callback_data='B'))
            markup.add(types.InlineKeyboardButton(floor_mat1[1], callback_data='F'))
            bot.send_message(message.chat.id, text, reply_markup=markup)

    @bot.callback_query_handler(func=lambda c: c.data in ['B', 'F'])
    def floor_mat(c):
        if c.data == "B":
            b.floor_k = 1.74
            print(1.74)
        else:
            b.floor_k = 1.92
            print(1.92)
        bot.send_photo(c.message.chat.id, "https://cch-rc.com/wp-content/uploads/2018/05/wall.jpg")
        bot.send_message(c.message.chat.id, "Введите толщину стен:")
        bot.register_next_step_handler(c.message, wall)

    def wall(message):
        if is_nvalue(message.text, 1):
            bot.send_message(message.chat.id, 'К сожалению вы неправильно ввели данные:( Попробуйте снова!')
            bot.send_photo(message.chat.id, "https://cch-rc.com/wp-content/uploads/2018/05/wall.jpg")
            bot.send_message(message.chat.id, "Введите толщину стен:")
            bot.register_next_step_handler(message, wall)
        else:
            b.thick_wall = float(message.text)
            text = "Выберите материал стен:"
            wall_mat1 = ["Пенобетон", "Кирпич", "Дерево"]
            markup = types.InlineKeyboardMarkup(row_width=2)
            markup.add(types.InlineKeyboardButton(wall_mat1[0], callback_data='P'))
            markup.add(types.InlineKeyboardButton(wall_mat1[1], callback_data='C'))
            markup.add(types.InlineKeyboardButton(wall_mat1[2], callback_data='S'))
            bot.send_message(message.chat.id, text, reply_markup=markup)

    @bot.callback_query_handler(func=lambda c: c.data in ['P', 'C', 'S'])
    def wall_mat(c):
        if c.data == "P":
            b.wall_k = 0.48
            print(0.48)
        elif c.data == "C":
            b.wall_k = 0.6
            print(0.6)
        else:
            b.wall_k = 0.29
            print(0.29)
        bot.send_photo(c.message.chat.id, "https://yandex.ru/images/touch/search?p=1&source=serp&text=%D0%BA%D1%80%D1%8B%D1%88%D0%B0+%D0%B3%D1%80%D0%B0%D1%84%D0%B8%D1%87%D0%B5%D1%81%D0%BA%D0%B0%D1%8F+%D0%BA%D0%B0%D1%80%D1%82%D0%B8%D0%BD%D0%BA%D0%B0&pos=16&clid=2332536&ui=webmobileapp.yandex&rpt=simage&app_platform=android&img_url=https%3A%2F%2Fgrizly.club%2Fuploads%2Fposts%2F2023-02%2F1676438346_grizly-club-p-krovelnie-raboti-klipart-10.png&app_version=24010600&lr=213&app_id=ru.yandex.searchplugin")
        bot.send_message(c.message.chat.id, "Введите толщину крыши:")
        bot.register_next_step_handler(c.message, roof)

    def roof(message):
        if is_nvalue(message.text, 1):
            bot.send_message(message.chat.id, 'К сожалению вы неправильно ввели данные:( Попробуйте снова!')
            bot.send_photo(message.chat.id, "https://yandex.ru/images/touch/search?p=1&source=serp&text=%D0%BA%D1%80%D1%8B%D1%88%D0%B0+%D0%B3%D1%80%D0%B0%D1%84%D0%B8%D1%87%D0%B5%D1%81%D0%BA%D0%B0%D1%8F+%D0%BA%D0%B0%D1%80%D1%82%D0%B8%D0%BD%D0%BA%D0%B0&pos=16&clid=2332536&ui=webmobileapp.yandex&rpt=simage&app_platform=android&img_url=https%3A%2F%2Fgrizly.club%2Fuploads%2Fposts%2F2023-02%2F1676438346_grizly-club-p-krovelnie-raboti-klipart-10.png&app_version=24010600&lr=213&app_id=ru.yandex.searchplugin")
            bot.send_message(message.chat.id, "Введите толщину крыши:")
            bot.register_next_step_handler(message, roof)
        else:
            b.thick_roof = float(message.text)
            text = "Выберите материал крыши:"
            roof_mat1 = ["Дерево", "ОСП", "ФСФ"]
            markup = types.InlineKeyboardMarkup(row_width=2)
            markup.add(types.InlineKeyboardButton(roof_mat1[0], callback_data='Wood'))
            markup.add(types.InlineKeyboardButton(roof_mat1[1], callback_data='OSB'))
            markup.add(types.InlineKeyboardButton(roof_mat1[2], callback_data='FSF'))
            bot.send_message(message.chat.id, text, reply_markup=markup)

    @bot.callback_query_handler(func=lambda c: c.data in ['Wood', 'OSB', 'FSF'])
    def roof_mat(c):
        if c.data == "Wood":
            b.roof_k = 0.18
            print(0.18)
        elif c.data == "FSF":
            b.roof_k = 0.048
            print(0.048)
        else:
            b.roof_k = 0.13
            print(0.13)
        bot.send_photo(c.message.chat.id, "https://sun9-34.userapi.com/impg/mABu9lmAwHlSM5btrQttHb-pMhsbRT8_EiwDCw/aIuU2gk4R4c.jpg?size=882x1080&quality=96&sign=823f7c9754b3e2d8bda340aa540a57e1&c_uniq_tag=vRNT0HnSPz5i9rCPxbXXvrnJLHuZ33x5NB5pvmYGTaQ&type=album")
        bot.send_message(c.message.chat.id, "Введите количество окон, их длину, ширину и толщину через пробел:")
        bot.register_next_step_handler(c.message, window)

    def window(message):
        if is_nvalue(message.text, 4):
            bot.send_message(message.chat.id, 'К сожалению вы неправильно ввели данные:( Попробуйте снова!')
            bot.send_photo(message.chat.id, "https://sun9-34.userapi.com/impg/mABu9lmAwHlSM5btrQttHb-pMhsbRT8_EiwDCw/aIuU2gk4R4c.jpg?size=882x1080&quality=96&sign=823f7c9754b3e2d8bda340aa540a57e1&c_uniq_tag=vRNT0HnSPz5i9rCPxbXXvrnJLHuZ33x5NB5pvmYGTaQ&type=album")
            bot.send_message(message.chat.id, "Введите количество окон, их длину, ширину и толщину через пробел:")
            bot.register_next_step_handler(message, window)
        else:
            lw = message.text.split()
            b.count_w = int(lw[0])
            b.len_w = float(lw[1])
            b.wide_w = float(lw[2])
            b.thick_w = float(lw[3])
            b.window_k = 0.76
            b.s_win = b.count_w * a.Square(b.len_w, b.wide_w)
            bot.send_message(message.chat.id, 'Суммарная площадь окон = {}'.format(b.s_win))
            bot.send_photo(message.chat.id, "https://ru.freepik.com/free-photos-vectors/%D0%B4%D0%B2%D0%B5%D1%80%D1%8C-3%D0%B4")
            bot.send_message(message.chat.id, "Введите количество дверей, выходящих наружу, их длину, ширину и толщину через пробел:")
            bot.register_next_step_handler(message, door)

    def door(message):
        if is_nvalue(message.text, 4):
            bot.send_message(message.chat.id, 'К сожалению вы неправильно ввели данные:( Попробуйте снова!')
            bot.send_photo(message.chat.id, "https://ru.freepik.com/free-photos-vectors/%D0%B4%D0%B2%D0%B5%D1%80%D1%8C-3%D0%B4")
            bot.send_message(message.chat.id, "Введите количество дверей, выходящих наружу, их длину, ширину и толщину через пробел:")
            bot.register_next_step_handler(message, door)
        else:
            lw = message.text.split()
            b.count_d = int(lw[0])
            b.len_d = float(lw[1])
            b.wide_d = float(lw[2])
            b.thick_d = float(lw[3])
            b.s_d = b.count_d * a.Square(b.len_d, b.wide_d)
            bot.send_message(message.chat.id, 'Суммарная площадь дверей, выходящих наружу = {}'.format(b.s_d))
            b.s_wall = a.Square_wall(b.len, b. wide, b.high, b.s_win, b.s_d)
            bot.send_message(message.chat.id, 'Суммарная площадь стен, без учёта дверей и окон = {}'.format(b.s_wall))
            text = "Выберите материал дверей:"
            door_mat1 = ["Металл", "Пластик", "Дерево", "Стекло"]
            markup = types.InlineKeyboardMarkup(row_width=2)
            markup.add(types.InlineKeyboardButton(door_mat1[0], callback_data='M'))
            markup.add(types.InlineKeyboardButton(door_mat1[1], callback_data='Pl'))
            markup.add(types.InlineKeyboardButton(door_mat1[2], callback_data='W'))
            markup.add(types.InlineKeyboardButton(door_mat1[3], callback_data='G'))
            bot.send_message(message.chat.id, text, reply_markup=markup)

    @bot.callback_query_handler(func=lambda c: c.data in ['M', 'Pl', 'W', 'G'])
    def door_mat(c):
        if c.data == "M":
            b.door_k = 45
            print(45)
        elif c.data == "Pl":
            b.door_k = 0.3
            print(0.3)
        elif c.data == "W":
            b.door_k = 0.18
            print(0.18)
        else:
            b.door_k = 0.76
            print(0.76)
        b.q_floor = a.Heat_loss(b.floor_k, b.s, b.thick_floor)
        b.q_wall = a.Heat_loss(b.wall_k, b.s_wall, b.thick_wall)
        b.q_roof = a.Heat_loss(b.roof_k, b.s, b.thick_roof)
        b.q_win = a.Heat_loss(b.window_k, b.s_win, b.thick_w)
        b.q_door = a.Heat_loss(b.door_k, b.s_d, b.thick_d)
        b.Q = round(b.q_wall + b.q_door + b.q_win + b.q_floor + b.q_roof,2)
        bot.send_photo(c.message.chat.id, "https://avatars.dzeninfra.ru/get-zen_doc/4481244/pub_60644be0f57165397e3790be_60644e4f4fcbbf222b11781d/scale_1200")
        bot.send_message(c.message.chat.id, 'Суммарные теплопотери = {}'.format(b.Q))
        b.P = math.ceil(a.Power(b.s, b.Q)/1000)
        bot.send_photo(c.message.chat.id, "https://domkotlov.by/photo/montazh-2021-02-09~elektrokotel_skat_p9k-skat~elektrokotel_skat_p6k-skat~montazh-ustanovka-obvyazka_kotla_montazh-yelektricheskogo-kotla~dom-kotlov-364-2.jpg")
        bot.send_message(c.message.chat.id, 'Расчётная мощность котла(кВт) = {}'.format(b.P))
        b.W = 13.5*b.P
        bot.send_photo(c.message.chat.id, "https://chelyabinsk.n-resource.ru/upload/iblock/599/5998c1d680bc5c4c0b5dd0351b667ced.png")
        bot.send_message(c.message.chat.id, 'Количество теплоносителя в системе(л) = {}'.format(b.W))
        b.V = (0.86*0.9*b.P)/20
        bot.send_message(c.message.chat.id, 'Скорость теплоносителя = {}'.format(b.V))
        bot.send_message(c.message.chat.id, 'Полный оборот всего теплоносителя в системе(раза в час) = {}'.format(round(b.V/b.W,2)))

import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType

from tokens import vk_token
import text_for_bot
from send_mail import mail_send
from flask_read_db import add_sql, app

vk_session = vk_api.VkApi(token=vk_token)
session_api = vk_session.get_api()
longpoll = VkLongPoll(vk_session)
orders = False
aderess_flag = False
choice = False
choice1 = False
numb = 0
summa = 0
aderess = ""
zakaz = []


def sender(id_u, text):
    vk_session.method("messages.send", {'user_id': id_u, 'message': text, 'random_id': 0})


for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW:
        if event.to_me:
            msg = event.text.lower()
            id_us = event.user_id
            if "!help" == msg:
                sender(id_us, text_for_bot.helper)
            elif "!menu" == msg:
                sender(id_us, text_for_bot.menu_to)
            elif "!order_info" == msg:
                sender(id_us, text_for_bot.order_ins)
            elif "!order" == msg:
                sender(id_us, text_for_bot.ask)
                choice = True
            elif choice:
                if msg == text_for_bot.yes:
                    orders = True
                    choice = False
                    sender(id_us, text_for_bot.start_ord)
                else:
                    choice = False
                    sender(id_us, text_for_bot.bad_text)
            elif "!pizza" in msg and orders:
                zakaz = msg[6:]
                zakaz = zakaz.split(",")
                zakaz = list(map(lambda x: x.strip(), zakaz))
                for piz in zakaz:
                    if piz in text_for_bot.menu:
                        summa += text_for_bot.menu[piz]
                    else:
                        sender(id_us, text_for_bot.order_fail)
                        orders = False
                        summa = 0
                        break
                if orders:
                    sender(id_us, text_for_bot.text_adres)
                    orders = False
                    aderess_flag = True
            elif aderess_flag:
                aderess = msg
                sender(id_us, text_for_bot.fin(summa, aderess))
                aderess_flag = False
                choice1 = True
            elif choice1:
                if msg == text_for_bot.yes:
                    choice1 = False
                    sender(id_us, text_for_bot.order_fin)
                    mail_send(id_us, summa, aderess, zakaz)
                    add_sql(numb, int(id_us), str(aderess))
                    numb += 1
                else:
                    choice1 = False
                    sender(id_us, text_for_bot.bad_text)
            else:
                sender(id_us, text_for_bot.dont_understand)

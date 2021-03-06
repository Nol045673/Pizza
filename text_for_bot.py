menu = {"маргарита": 150,
        "гавайская": 200,
        "четыре сыра": 180,
        "карбонара": 150,
        "мексиканская": 170,
        "пепперони": 160}
menu_to = "'Меню:\n Маргарита - 150р\n Гавайская - 200р\n Четыре сыра - 180р\n Карбонара - 150р\n Мексиканская - 170р\n Пепперони - 160р\n !Все пиццы по 35 см диаметром!'"
helper = "Вас приветсвует раздел помощи!\n Доступны команды:\n !menu (Все доступные пиццы)\n !order_info (Инструкция как оформить заказ)\n !order (Оформление заказа, с ответом да или нет)\n !pizza (доступен при оформлении заказа)"
order_ins = "Вас приветсвует раздел заказа!\n Чтобы оформить заказ необходимо с помощью команды !order и в !pizza перечислить выбранные вами пиццы через запятую. Если данные указаны верно, то вам поступит сообщение, где следует написать свой адресс."
order_fail = "В заказе присутствуют неверные названия или перечисление происходило без запятой. Заказ сброшен. Для повтора введите ещё раз команду !order"
text_adres = "Введите адрес. Достоверность адреса оставляем на вас."
order_fin = "Заказ оформлен. Оплата происходит у курьера.\n Приятного аппетита!"
bad_text = "Оформление заказа сброшено. Вы ответили нет или что-то другое. Для оформления заказа введите !order"
dont_understand = "Не понимаю."
start_ord = "Приступайте к выбору пиццы с помощью команды !pizza."
ask = "Вы согласны оформить заказ?"
yes = "да"


def fin(summa, aderess):
    return f"Ваш заказ вышел на сумму: {summa}.\n И будет отправлен по адресу: {aderess}.\n Вы согласны? Ответ да или нет. Если ввод будет неверен - заказ сбросится(Убедитесь что все написано верно)"

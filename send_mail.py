import smtplib
import ssl
from tokens import password_mail
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def mail_send(id_u, summa, addres, zakaz):
    msg = MIMEMultipart()
    port = 587
    login = "botpizzavk@gmail.com"
    password = password_mail
    url = "smtp.gmail.com"
    toaddr = "nol034@yandex.ru"
    msg['Subject'] = "Order_vk"
    body = f"id: {id_u}\nRub: {summa}\nAddress: {addres}\nPizza: {zakaz}"
    msg.attach(MIMEText(body, 'plain'))
    contaext = ssl.create_default_context()
    with smtplib.SMTP(url, port) as server:
        server.starttls(context=contaext)
        server.login(login, password)
        server.sendmail(login, toaddr, msg.as_string())
        server.quit()
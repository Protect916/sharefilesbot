import telebot
import time
import config
import os
from telebot import types

bot = telebot.TeleBot(config.token)


@bot.message_handler(commands=['get223']) #/get223
def find_file_ids(message):
    bot.reply_to(message, "Подготовка файла...")
    for file in os.listdir('kangi/'):
        if file.split('.')[-1] == 'mp3':
            f = open('kangi/'+file, 'rb')
            msg = bot.send_audio(message.chat.id, f, None)
            bot.reply_to(message, "Файл успешно отправлен! С уважением проект @dleteam")
        time.sleep(3)


@bot.message_handler(commands=['get283'])
def find_file_ids(message):
    bot.reply_to(message, "Подготовка файла...")
    for file in os.listdir('rh/'):
        if file.split('.')[-1] == 'mp3':
            f = open('rh/'+file, 'rb')
            msg = bot.send_audio(message.chat.id, f, None)
            bot.reply_to(message, "Файл успешно отправлен! С уважением проект @dleteam")
        time.sleep(1)


@bot.message_handler(commands=['get593'])
def find_file_ids(message):
    bot.reply_to(message, "Подготовка файла...")
    for file in os.listdir('unceflexx/'):
        if file.split('.')[-1] == 'ogg':
            f = open('unceflexx/'+file, 'rb')
            msg = bot.send_audio(message.chat.id, f, None)
            bot.reply_to(message, "Файл успешно отправлен! С уважением проект @dleteam")
        time.sleep(3)


@bot.message_handler(commands=['get553'])
def find_file_ids(message):
        f = open('unceflexx/t562640772_s0.jpg', 'rb')
        msg = bot.send_photo(message.chat.id, f, None)



@bot.message_handler(commands=['get969'])
def find_file_ids(message):
    bot.reply_to(message, "Подготовка файла...")
    for file in os.listdir('prvt2/'):
        if file.split('.')[-1] == 'mp3':
            f = open('prvt2/'+file, 'rb')
            msg = bot.send_audio(message.chat.id, f, None)
            bot.reply_to(message, "Файл успешно отправлен! С уважением проект @dleteam")
        time.sleep(3)


@bot.message_handler(commands=['get962'])
def find_file_ids(message):
    bot.reply_to(message, "Подготовка файла...")
    for file in os.listdir('prvt1/'):
        if file.split('.')[-1] == 'mp3':
            f = open('prvt1/'+file, 'rb')
            msg = bot.send_audio(message.chat.id, f, None)
            bot.reply_to(message, "Файл успешно отправлен! С уважением проект @dleteam")
        time.sleep(3)


@bot.message_handler(commands=['mayot'])
def find_file_ids(message):
    for file in os.listdir('mayot/'):
        if file.split('.')[-1] == 'mp3':
            f = open('mayot/'+file, 'rb')
            msg = bot.send_audio(message.chat.id, f, None)
            bot.reply_to(message, "Файлы успешно отправлены! С уважением проект @dleteam")
        time.sleep(3)


@bot.message_handler(commands=['buy'])
def find_file_ids(message):
    bot.send_message(admin_id, 'Пользователь: {0.id}. Написал команлу /buy'.format(
        message.from_user, bot.get_me()),
                     parse_mode='html')
    bot.send_message(message.chat.id,
                     "<i>Подождите пожалуйста, идет генерация оплаты...</i>\n\nСсылка для оплаты, <b>просто вставьте ее в удобный для вас брузер:</b> \nhttps://new.donatepay.ru/@ml?name={0.id}&amount=80&currency=RUB&message=Покупка+привата+от+{0.first_name}".format(
                         message.from_user, bot.get_me()),
                     parse_mode='html')






@bot.message_handler(commands=['id'])
def find_file_ids(message):
    bot.send_message(admin_id, 'Пользователь: {0.id}. Написал команлу /id'.format(
        message.from_user, bot.get_me()),
                     parse_mode='html')
    bot.send_message(message.chat.id,
                     "<i>Твой айди:</i><b> {0.id}</b>\n<i>Твой юзернейм:</i><b> {0.username}</b> ".format(
                         message.from_user, bot.get_me()),
                     parse_mode='html')

@bot.message_handler(commands=['help'])
def find_file_ids(message):
    bot.send_message(admin_id, 'Команда: /help\n\nИнформация о пользователе:\n<b>ID: {0.id}\nПолное имя профиля: {0.first_name}\nНикнейм: {0.username}</b>'.format(
        message.from_user, bot.get_me()),
                     parse_mode='html')
    bot.send_message(message.chat.id, "/help - <b>Вызвать это меню</b>\n/buy - <b>Купить приват</b>\n<i>Для получения файлов, указывайте команду из канала</i>".format(
                         message.from_user, bot.get_me()),
                     parse_mode='html')





@bot.message_handler(content_types=['text'])
def send_id(message):
    if message.text.lower() == 'приват':
        bot.send_message(message.chat.id, 'Купить приват - @gangst616')
if __name__ == '__main__':
    bot.infinity_polling()

















import telebot
import time
import config

bot = telebot.TeleBot(config.token)


@bot.message_handler(content_types=['text'])  # НЕ МЕНЯТЬ!
def get_file(message):
    if message.chat.type == 'private':

        if message.text == '/start aK52':
            bot.send_message(message.chat.id,
                             "Подождите, идет загрузка вашего файла...")
            time.sleep(1)
            f = open("Ваш путь + название файла", 'rb')
            msg = bot.send_audio(message.chat.id, f, None)


if __name__ == '__main__':
    bot.infinity_polling()

 #script by protect

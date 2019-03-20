#!/usr/bin/python3
from telegram.ext import Updater, InlineQueryHandler, CommandHandler
import requests
import re

def get_url():
    contents = requests.get('https://random.dog/woof.json').json()
    url = contents['url']
    return url

def get_image_url():
    allowed_extension = ['jpg','jpeg','png']
    file_extension = ''
    while file_extension not in allowed_extension:
        url = get_url()
        file_extension = re.search("([^.]*)$",url).group(1).lower()
    return url
def get_gif_url():
    allowed_extension = ['gif','mp4']
    file_extension = ''
    while file_extension not in allowed_extension:
        url = get_url()
        file_extension = re.search("([^.]*)$",url).group(1).lower()
    return url
def bop(bot, update):
    url = get_image_url()
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)

def bop_gif (bot,update):
    url=get_gif_url()
    chat_id = update.message.chat_id
    bot.send_animation(chat_id=chat_id,animation=url)
def main():
    updater = Updater('785931989:AAF--IVd_UmXvs-swFEzXP6VlvrNGVlWkTw')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    dp.add_handler(CommandHandler('bop_gif',bop_gif))
    dp.add_handler(CommandHandler('help',help))
    dp.add_handler(CommandHandler('Love',I_love))
    updater.start_polling()
    updater.idle()
def help (bot,update):
    chat_id = update.message.chat_id
    bot.sendMessage(chat_id=chat_id,text="\t/help для вызова этого меню \n\t/bop для фота собачек \n\t/bop_gif для гифки\n\tА таже тут есть пасхалка")
def I_love(bot,update):
    chat_id = update.message.chat_id
    bot.sendMessage(chat_id=chat_id,text="А я люблю собак :-)")

if __name__ == '__main__':
    main()

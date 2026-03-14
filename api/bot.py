from django.conf import settings
from telegram import Bot, Update
from telegram.ext import Dispatcher, CommandHandler

from .handlers import start, login


bot = Bot(settings.TG_BOT_TOKEN)
dispatcher = Dispatcher(bot, None, workers=4, use_context=True)

dispatcher.add_handler(CommandHandler('start', start))
dispatcher.add_handler(CommandHandler('login', login))


def handle_update(data: dict):
    update = Update.de_json(data, bot)
    dispatcher.process_update(update)


def set_webhook(url: str):
    bot.set_webhook(url)

#!/usr/bin/python3
# -*- coding: utf-8 -*-
from lxml import etree
from telegram import (ReplyKeyboardMarkup, ReplyKeyboardRemove)
from telegram.ext import (Updater, CommandHandler, MessageHandler, Filters, RegexHandler,
                          ConversationHandler)
import logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
level=logging.INFO)

logger = logging.getLogger(__name__)

def start(bot, update):
    log_params('help', update)
    update.message.reply_text(
        'Hi! My name is Professor Bot. I will hold a conversation with you. '
        'Send /cancel to stop talking to me.\n\n'
        'Are you a boy or a girl?')


def error(bot, update, error):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, error) 
def main():
    logger.setLevel(logging.DEBUG)
    cfg = etree.parse('./config.xml') 
    cfgroot=cfg.getroot()
    telegram_param=cfgroot.find('telegram')  
    tg_token=telegram_param.find('token').text  
    updater = Updater(tg_token)
    dp = updater.dispatcher
    updater.start_polling()
    updater.idle()
if __name__ == "__main__":
    main()

#!/usr/bin/python
from lxml import etree
def start(bot, update):
    reply_keyboard = [['Boy', 'Girl', 'Other']]

    update.message.reply_text(
        'Привет я робот судебный пристав. '
        'Чем могу быть полезен?'
        '',
        reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True))

    return 
def main():
    cfg = etree.parse(f) 
    cfgroot=cfg.getroot()
    telegram_param=cfgroot.find('telegram')  
    tg_token=telegram_param('token').text  
    updater = Updater(tg_token)
    dp = updater.dispatcher
    updater.start_polling()
    updater.idle()
if __name__ == "__main__":
    main()

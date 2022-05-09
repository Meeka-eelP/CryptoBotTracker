import telegram
from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext.updater import Updater
from telegram.update import Update
from telegram.ext.callbackcontext import CallbackContext
from telegram.ext.commandhandler import CommandHandler
from telegram.ext.messagehandler import MessageHandler
from telegram.ext.filters import Filters

from tracker import get_prices
from tracker import get_sat

telegram_bot_token = "5123008011:AAGMDse5bkMjp6eMv7uEwUzAEvz8PS2eQaU"

updater = Updater(token=telegram_bot_token, use_context=True)
dispatcher = updater.dispatcher

#Define commands
def start(update, context):
        chat_id = update.effective_chat.id
        #message = ""
        update.message.reply_text("Hey! Welcome to the Crypto Price Tracker bot. Type /help for a list of commands")

def help(update: Update, context: CallbackContext):
        update.message.reply_text("Here is a list of available commands : \n/start : To go back to the main menu\n/all : To view all crypto prices\n/help : To view the list of commands again")

#def unknown_text(update: Update, context: CallbackContext):
#    update.message.reply_text(
#        "Sorry I can't recognize you , you said '%s'" % update.message.text)

def all(update, context):
        chat_id = update.effective_chat.id
        message = ""

        btc_data = get_sat()
        for x in btc_data:
                btc_price = btc_data[x]["price"]
#               print(btc_price)
                one_sat = btc_price/100000000
#               print(one_sat)

        crypto_data = get_prices()

        for i in crypto_data:
                coin = crypto_data[i]["coin"]
                price = crypto_data[i]["price"]
                price_in_sats = ((price*(1/one_sat)))/100000000
                change_day = crypto_data[i]["change_day"]
                change_hour = crypto_data[i]["change_hour"]
                message += f"Coin: {coin}\nPrice: ${price:,.2f}\nValue in Satoshis: {price_in_sats:.8f}\nHour Change: {change_hour:.3f}%\nDay Change: {change_day:.3f}%\n\n"

        context.bot.send_message(chat_id=chat_id, text=message)

dispatcher.add_handler(CommandHandler("start", start))
dispatcher.add_handler(CommandHandler("help", help))
dispatcher.add_handler(CommandHandler("all", all))

#updater.dispatcher.add_handler(MessageHandler(Filters.text, unknown_text))

updater.start_polling()

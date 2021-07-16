import os
import query
import telebot
import time
import threading
from keep_alive import keep_alive

print("start")
keep_alive()
# bot = telebot.TeleBot("1657139126:AAFSFRVGofn0Zb3MlEtvU28yCq2QQqIiUdg")

# @bot.message_handler(commands=['start', 'help'])
# def send_welcome(message):
# bot.reply_to(message, "Howdy, how are you doing?")


# @bot.message_handler(func=lambda message: True)
# def echo_all(message):
# bot.reply_to(message, message.text)

# while True:
# print("blabla")
# try:
# print("polling")
##bot.polling()
# print("polling2")
# except Exception:
# time.sleep(10)
# print("not polling")


BOT_TOKEN = "1657139126:AAFSFRVGofn0Zb3MlEtvU28yCq2QQqIiUdg"
BOT_INTERVAL = 3
BOT_TIMEOUT = 30


# bot = None #Keep the bot object as global variable if needed

def bot_polling():
    # global bot #Keep the bot object as global variable if needed
    print("Starting bot polling now")
    while True:
        try:
            print("New bot instance started")
            bot = telebot.TeleBot(BOT_TOKEN)  # Generate new bot instance
            botactions(bot)  # If bot is used as a global variable, remove bot as an input param
            bot.polling(none_stop=True, interval=BOT_INTERVAL, timeout=BOT_TIMEOUT)
        except Exception as ex:  # Error in polling
            print("Bot polling failed, restarting in {}sec. Error:\n{}".format(BOT_TIMEOUT, ex))
            bot.stop_polling()  #
            time.sleep(BOT_TIMEOUT)
        else:  # Clean exit
            bot.stop_polling()
            print("Bot polling loop finished")
            break  # End loop


def botactions(bot):
    # Set all your bot handlers inside this function
    # If bot is used as a global variable, remove bot as an input param
    @bot.message_handler(commands=['price'])
    def send_price(message):
        s = query.create_message_price()
        while True:
            try:
                bot.reply_to(message, s, parse_mode="MarkdownV2")
                print("All good")
                break
            except Exception:
                print("Oops!  Message wasn't sent... trying again")


polling_thread = threading.Thread(target=bot_polling)
polling_thread.daemon = True
polling_thread.start()

# Keep main program running while bot runs threaded
if __name__ == "__main__":
    while True:
        try:
            print("2min")
            time.sleep(120)
        except KeyboardInterrupt:
            break


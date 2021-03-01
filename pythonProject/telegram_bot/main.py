import telebot

import say_bot
import emojis

bot = telebot.TeleBot("", parse_mode = None)

@bot.message_handler(commands = ['start', 'hello'])
def send_message(message):
    username = message.from_user.first_name
    bot.reply_to(message, f"{say_bot.say_bot()} {username} {emojis.happy()}")




bot.polling()
print('bot running')
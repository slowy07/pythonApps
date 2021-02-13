import telebot

import say_bot
import emojis

bot = telebot.TeleBot("1360881292:AAG-z5HAc88OWkjmg7yJXSDzhOokp1VMrB0", parse_mode = None)

@bot.message_handler(commands = ['start', 'hello'])
def send_message(message):
    username = message.from_user.first_name
    bot.reply_to(message, f"{say_bot.say_bot()} {username} {emojis.happy()}")




bot.polling()
print('bot running')
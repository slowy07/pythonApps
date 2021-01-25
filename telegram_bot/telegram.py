import telebot

bot = telebot.Telebot(token='your_token_here')


##sayhi bot while typing /start
@bot_message_handler(commands=['start'])
def bot_sayhi(message):
    bot.reply_to(message,"hello !")

## custom text input
@bot_message_handler(func=lambda message: True)
def say_bot(message):
    custom_message = message.text
    
    if custom_message == 'hello there':
        bot.reply_to(message, "hello there you are !")
    else:
        bot.reply_to(message, "still searching !")

print('bot is running!')
bot.polling()

"""
>>bot is running!
"""
import random

#---get bot say message from bot_message.txt
def say_bot():
    file = open('bot_message.txt')
    data_bot = file.readlines()
    say_bot_list = []
    for saybot in data_bot:
        say_bot_list.append(saybot.strip())
        
    return random.choice(say_bot_list)
#------------------------------------------------
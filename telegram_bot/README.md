## installation telegram bot

- open telegram apps and add `@BotFather`
- for create new bots type `/newbot` and automatically BotFather will send message for create new bot and will ask name of your bot
- create a name for your bot by just typing and send it, example `edith` and then Bot Father will ask you for bot username
- create username for your bot, example `edith_bot`, create name must with `somethingString_bot` if username already exists, you must create a new one
- and your bot was added, BotFather will message for information bot API and token for your bot

## bot usefull commands

- `/newbot` = create a new bot
- `/mybots` = list your bots
- `/setname` = change name your bots
- `/setdescription` = change / add description for your bots
- `/setuserpic` = change / add bots photo profile
- `/setcommands` = change the list of commands
- `/deletebot` = delete a bots

## python installation

commands installation

```bash
pip install telebot
```

for simple bot message

```python
import telebot

bot = telebot.Telebot(token='your_bot_token_here')

@bot_message_handler(commands=['start'])
def send_message_to_user(message):
    bot.reply_to(message, "hello !")

print('bot running!')
bot.polling()
```

and then running and back to telegram and start chat with your bots by sending `/start`
your bot will send you message `hello!`

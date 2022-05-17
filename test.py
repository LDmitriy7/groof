from async_tg_bot import Bot
from async_tg_bot.methods import *
import logging

bot = Bot()  # token loaded from $BOT_TOKEN


@bot.on_message(command='start')
def start():
    return SendMessage(text='Hello')


@bot.task()
def start():
    res = SendMessage(text='Hello', chat_id=724477101).request()
    print(f'{res = }')


logging.basicConfig(
    level=20,
)

if __name__ == '__main__':
    bot.run()
    bot.logger.info('End!')

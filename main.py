from aiogram import Bot, types, executor, Dispatcher

bot = Bot('YOUR TOKEN')
dp = Dispatcher(bot)


@dp.message_handler(commands=['start']) # Handler to the start command
async def start(message: types.Message): # asynchronous function
    await bot.send_message(message.chat.id, 'Your Message for command /START')

@dp.message_handler(commands=['help']) # Handler to the help command
async def help(message: types.Message): # asynchronous function
    await bot.send_message(message.chat.id, 'Your Help message')


# Here we do a check for the message you want, example : 
# if message == Hello: then the bot sends Hello
@dp.message_handler(content_types=['text'])
async def anyonetext(message: types.Message): # asynchronous function
    if message.text == 'Hi':
        await bot.send_message(message.chat.id, 'Hello!')
    # elif
    # elif

if __name__ == '__main__': # setup our bot
    executor.start_polling(dp, skip_updates=True ) # skip_updates = skip anyone message when bot are off
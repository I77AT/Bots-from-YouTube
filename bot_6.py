# pip install aiogram==2.25.2

from aiogram import Bot, Dispatcher, executor, types

bot = Bot('')
dp = Dispatcher(bot)

@dp.message_handler(content_types=['photo'])
async def start(message:types.Message):
    # await message.answer('hello')
    # await bot .send_message(message.chat.id,'hello')
    await message.reply('hello')

@dp.message_handler(commands=['inline'])
async def info(message:types.Message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('Site',url='https://classroom.google.com/'))
    markup.add(types.InlineKeyboardButton('Hello',callback_data='hello'))
    await message.reply('Hello',reply_markup=markup)

@dp.callback_query_handler()
async def callback(call):
    await call.message.answer(call.data)

@dp.message_handler(commands=['reply'])
async def reply(message:types.Message):
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
    markup.add(types.KeyboardButton('Site'))
    markup.add(types.KeyboardButton('WebSite'))
    await message.answer('hello',reply_markup=markup)


executor.start_polling(dp)


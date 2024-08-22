import asyncio
import logging
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram import Bot, Dispatcher,types,F 
from aiogram.types import Message
from aiogram.filters import Command,CommandStart
from config import token
from parsing3 import all_news
from db3 import Database

bot = Bot(token=token)
dp = Dispatcher()
db=Database('news.db')
db.create_table()
stoped_parsing = asyncio.Event()


logging.basicConfig(level=logging.INFO)

class Form(StatesGroup):
    news = State()
    stop=State()

start_buttons = [
    [types.KeyboardButton(text='news') ],
    [types.KeyboardButton(text='stop')]
]

start_keyboard = types.ReplyKeyboardMarkup(keyboard=start_buttons, resize_keyboard=True)

@dp.message(CommandStart())
async def start(message:Message,state:FSMContext):
    await state.set_state(Form.news)
    await message.answer("нажми на новость что бы прочитать новости\nнажми на ОСТАНОВИТЬ что бы остановить",reply_markup=start_keyboard)
 

@dp.message(Command('stop'))
async def stop(message: Message):
    stoped_parsing.set()
    await message.answer("Парсинг новостей будет остановлен.", reply_markup=start_keyboard)


@dp.message(Form.news,F.text)
async def about_news(message:Message): 
    stoped_parsing.clear()      
    s=0
    for news in all_news: 
        if stoped_parsing.is_set():
          await message.answer("Парсинг новостей остановлен.", reply_markup=start_keyboard)
          break      
        s+=1
        db.add_news(news.text)    
        await message.answer(f'{s}.{news.text}')      
  



async def main():
    await dp.start_polling(bot)
    
if __name__ == "__main__":
    asyncio.run(main())
import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from config import TOKEN
import random

from config import TOKEN

bot = Bot(token=TOKEN)                           # шифрованный токен
dp = Dispatcher()                                # обработчик сообщений

#Прописываем хендлер и варианты ответов:

@dp.message(Command('photo'))
async def photo(message: Message):
    list = ['https://i.pinimg.com/736x/22/e1/7c/22e17c5cb7399995f829111676a5e03d.jpg', 'https://rc-today.ru/UserFiles/Image/Big/img105587_64222_big.jpg', 'https://i.pinimg.com/736x/fc/f1/ce/fcf1ce3e1a93bd99cef2240bd52b9e39.jpg']
    rand_photo = random.choice(list)
    await message.answer_photo(photo=rand_photo, caption="Это супер крутая картинка")

@dp.message(F.photo)
async def react_photo(message: Message):
    list = ['Ого, какая фотка!', 'Непонятно, что это такое', 'Не отправляй мне такое больше']
    rand_answ = random.choice(list)
    await message.answer(rand_answ)

@dp.message(F.text == "Что такое ИИ?") # цикл обработки команд
async def aitext(message: Message): # цикл обработки сообщений
    await message.answer("ИИ (искусственный интеллект) — это область информатики и вычислительной техники, которая занимается созданием систем, способных выполнять задачи, требующие интеллекта, такие как понимание языка, обучение, рассуждение, решение проблем и адаптация к новым ситуациям.") # ответ на сообщение

@dp.message(Command('help')) # цикл обработки команд
async def help(message: Message): # цикл обработки сообщений
    await message.answer("Этот бот умеет выполнять эти команды : \n /start \n /help") # ответ на сообщение
                                                           # \n - перенос строки
@dp.message(CommandStart())                       # создание обработчика команд
async def start(message: Message):                # цикл обработки сообщений
    await message.answer("Приветики, я бот!")     # ответ на сообщение

async def main():                                  # цикл обработки сообщений
    await dp.start_polling(bot)                    # запуск обработки сообщений

if __name__ == '__main__':
    asyncio.run(main())
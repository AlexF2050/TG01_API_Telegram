import asyncio
from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from config import TOKEN


bot = Bot(token=TOKEN)                          # шифрованный токен
dp = Dispatcher()                               # обработчик сообщений

@dp.message(CommandStart())                     # создание обработчика команд
async def start(message: Message):              # цикл обработки сообщений
    await message.answer("Приветики, я бот!")   # ответ на сообщение



async def main():                               # цикл обработки сообщений
    await dp.start_polling(bot)                    # запуск обработки сообщений

if __name__ == '__main__':
    asyncio.run(main())
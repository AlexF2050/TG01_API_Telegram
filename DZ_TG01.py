import os
import requests
import logging
from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart, Command
from aiogram.types import Message

API_TOKEN = ('Добавьте токен')
WEATHER_API_KEY = ('Добавьте токен')

logging.basicConfig(level=logging.INFO)                 # Настройка логирования

bot = Bot(token=API_TOKEN)                              # Создание бота
dp = Dispatcher()                                       # Создание хендлера

@dp.message(CommandStart())                             # Хендлер с использованием CommandStart
async def start(message: Message):
    await message.answer("Доброго времени, я бот, который расскажет про погоду!")

@dp.message(Command(commands=["help"]))                 # Хендлер с использованием Command
async def help_command(message: Message):
    await message.answer("Бот умеет выполнять команды:\n/start\n/help\n/weather")

@dp.message(Command(commands=["weather"]))              # хендлер для команды /weather
async def weather_command(message: Message):
    city = "Dikson"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={WEATHER_API_KEY}&units=metric&lang=ru"
    response = requests.get(url)
    data = response.json()

    if data["cod"] == 200:                              # Если код ответа 200 - удачное выполнение
        temperature = data["main"]["temp"]              # температура
        description = data["weather"][0]["description"] # описание
        await message.answer(f"Погода в {city.capitalize()}:\nТемпература: {temperature}°C\nОписание: {description}")
    else:
        await message.answer("Не удалось получить прогноз погоды. Пожалуйста, попробуйте позже.")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
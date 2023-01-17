# import csv
import json
import random
from os import system 
from time import sleep 
from datetime import datetime 

import requests 
from aiogram import Bot, types 
from aiogram.utils import executor 
from aiogram.dispatcher import Dispatcher
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton

# Created module - Созданный модуль
from core.config import TOKEN, ADMIN_ID, ADMIN_ID_INT
from core.static.sticker import S001, S002 
from core.newsalmaty import NewsAlmatyParser

system("clear")
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start']) 
async def start(message: types.Message):
    markup = ReplyKeyboardMarkup(resize_keyboard = True).add(
        KeyboardButton("Зарегистрируйтесь пожалуйста", request_contact = True)
    )
    photo_start = open("core/static/image/almaty.jpg", "rb")
    await message.reply_photo(photo = photo_start, caption="Свежие новости города Алматы и главные события в городе на сегодня ✅\n Последние новости ➜ Только актуальная информация про последние события и происшествия в\n Алмате на t.me/TengrinewsAlmatyBot!", reply_markup=markup)
    await message.answer(text = "Просим вас пройти регистрацию, для возможности пользования ботом!")

@dp.message_handler(content_types = types.ContentTypes.CONTACT)
async def registrations(message: types.Message):
    user_id = message.contact.user_id
    username = message.chat.username
    first_name = message.contact.first_name
    last_name = message.contact.last_name
    phone = message.contact.phone_number

    Informations = f"""id:{user_id}
username: @{username}
first_name:{first_name}
last_name: {last_name}
phone: {phone}
created: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}"""

    await bot.send_message(ADMIN_ID, Informations)
    markup = ReplyKeyboardMarkup(resize_keyboard = True).add(
        KeyboardButton("Запросить актульные новости"),
        KeyboardButton("свежие новости"),
        KeyboardButton("старые новости")
    )
    await message.reply_sticker(random.choice(S002))
    await message.answer("Вы успешно зарегистрированы", reply_markup = markup)

@dp.message_handler(content_types = ["text"])
async def news_today(message: types.Message):
    with open("core/json/news_almaty.json", "r") as file:
        all_news = json.load(file)
    
    if message.text.lower() == "запросить актульные новости":
        NewsAlmatyParser()

        news_almaty = []
        for item in all_news:
            item_title = item["title"]
            item_description = item["description"]
            item_url = item["url"]
            text = f"""{item_title}\n
{item_description}\n
{item_url}"""
            await message.answer(text = text)
            sleep(10)
        await message.reply_sticker(random.choice(S002))
        await message.answer("Это все новости на сегодня")
    elif message.text.lower() == "свежие новости":
        NewsAlmatyParser()

        news_almaty = []
        for item in all_news[:3]:
            item_title = item["title"]
            item_description = item["description"]
            item_url = item["url"]
            text = f"""{item_title}\n
{item_description}\n
{item_url}"""
            await message.answer(text = text)
            sleep(10)
        await message.reply_sticker(random.choice(S002))
        await message.answer("Это все новости на сегодня")
    elif message.text.lower() == "старые новости":
        NewsAlmatyParser()

        news_almaty = []
        for item in all_news[-3:]:
            item_title = item["title"]
            item_description = item["description"]
            item_url = item["url"]
            text = f"""{item_title}\n
{item_description}\n
{item_url}"""
            await message.answer(text = text)
            sleep(10)
        await message.reply_sticker(random.choice(S002))
        await message.answer("Это все новости на сегодня")
    else:
        await message.reply("Пока новостей нет")
if __name__ == "__main__":
    print("Бот запущен")
    executor.start_polling(dp)



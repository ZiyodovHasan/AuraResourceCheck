import logging
import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.filters import Command

TOKEN = "7585579146:AAFrnCNSxFrBCJaJc8ZooGg2fB79iPgk4wg"

bot = Bot(token=TOKEN)
dp = Dispatcher()

logging.basicConfig(level=logging.INFO)

@dp.message(Command("start"))
async def start_command(message: types.Message):
    await message.answer("Привет! Доступные команды:\n/plugins - Доступные плагины\n/site - Сайт сервера\n/telegram - Телеграм канал")

@dp.message(Command("plugins"))
async def plugins_command(message: types.Message):
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="📥 Скачать AuraResourceCheck", callback_data="download_AuraResourceCheck")],
        [InlineKeyboardButton(text="📥 Скачать AuraDonate", callback_data="download_AuraDonate")]
    ])
    await message.answer("Выберите плагин для скачивания:", reply_markup=keyboard)

@dp.callback_query()
async def handle_callback(query: types.CallbackQuery):
    if query.data == "download_AuraResourceCheck":
        await query.message.answer("🔗 Ссылка на скачивание AuraResourceCheck: [СКАЧАТЬ](https://example.com/AuraResourceCheck)", parse_mode="Markdown")
    elif query.data == "download_AuraDonate":
        await query.message.answer("🔗 Ссылка на скачивание AuraDonate: [СКАЧАТЬ](https://example.com/AuraDonate)", parse_mode="Markdown")
    await query.answer()

@dp.message(Command("site"))
async def site_command(message: types.Message):
    await message.answer("Сайт сервера пока недоступен.")

@dp.message(Command("telegram"))
async def telegram_command(message: types.Message):
    await message.answer("Официальный телеграм канал: https://t.me/auraway")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())

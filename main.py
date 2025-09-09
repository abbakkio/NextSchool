import asyncio
import os
from aiogram import Bot, Dispatcher, types
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from dotenv import load_dotenv

load_dotenv()

# Токен замени на свой
TOKEN = os.getenv("BOT_TOKEN")

bot = Bot(token=TOKEN)
dp = Dispatcher()

# --- Главное меню ---
def main_menu():
    kb = ReplyKeyboardBuilder()
    kb.button(text="📚 Учёба")
    kb.button(text="🏋️ Зал")
    kb.button(text="🎸 Хобби")
    kb.button(text="📖 Чтение")
    kb.button(text="⚙️ Настройки")
    kb.adjust(2)  # расположение кнопок (2 в ряд)
    return kb.as_markup(resize_keyboard=True)


@dp.message(Command("start"))
async def cmd_start(message: Message):
    await message.answer(
        "Привет! Это твой персональный помощник 🚀\nВыбери раздел из меню:",
        reply_markup=main_menu()
    )


# --- Обработчики кнопок ---
@dp.message(lambda m: m.text == "📚 Учёба")
async def study_section(message: Message):
    await message.answer("Раздел *Учёба* открыт ✏️", parse_mode="Markdown")

@dp.message(lambda m: m.text == "🏋️ Зал")
async def gym_section(message: Message):
    await message.answer("Раздел *Зал* 💪")

@dp.message(lambda m: m.text == "🎸 Хобби")
async def hobby_section(message: Message):
    await message.answer("Раздел *Хобби* 🎶")

@dp.message(lambda m: m.text == "📖 Чтение")
async def reading_section(message: Message):
    await message.answer("Раздел *Чтение* 📚")

@dp.message(lambda m: m.text == "⚙️ Настройки")
async def settings_section(message: Message):
    await message.answer("Раздел *Настройки* ⚙️")


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())

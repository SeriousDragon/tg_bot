import logging
import os
from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.filters.command import Command
import re

os.chdir(os.path.dirname(os.path.abspath(__file__)))

TOKEN = os.getenv("TOKEN")


bot = Bot(token=TOKEN)
dp = Dispatcher()
logging.basicConfig(
    level=logging.INFO,
    filename="bot.log",
    filemode="a",
    format="%(asctime)s - %(levelname)s - %(message)s",
)
print("Current working directory:", os.getcwd())


@dp.message(Command(commands=["start"]))
async def proccess_command_start(message: Message):
    user_name = message.from_user.full_name
    user_id = message.from_user.id
    text = f"Привет, {user_name}!\nНапиши имя и фамилию для транслитерации."
    logging.info(f"{user_name} c id {user_id} запустил бота")
    await bot.send_message(chat_id=user_id, text=text)


def transliterate(text: str) -> str:
    translit_dict = {
        "А": "A",
        "а": "a",
        "Б": "B",
        "б": "b",
        "В": "V",
        "в": "v",
        "Г": "G",
        "г": "g",
        "Д": "D",
        "д": "d",
        "Е": "E",
        "е": "e",
        "Ё": "E",
        "ё": "e",
        "Ж": "Zh",
        "ж": "zh",
        "З": "Z",
        "з": "z",
        "И": "I",
        "и": "i",
        "Й": "I",
        "й": "i",
        "К": "K",
        "к": "k",
        "Л": "L",
        "л": "l",
        "М": "M",
        "м": "m",
        "Н": "N",
        "н": "n",
        "О": "O",
        "о": "o",
        "П": "P",
        "п": "p",
        "Р": "R",
        "р": "r",
        "С": "S",
        "с": "s",
        "Т": "T",
        "т": "t",
        "У": "U",
        "у": "u",
        "Ф": "F",
        "ф": "f",
        "Х": "Kh",
        "х": "kh",
        "Ц": "Ts",
        "ц": "ts",
        "Ч": "Ch",
        "ч": "ch",
        "Ш": "Sh",
        "ш": "sh",
        "Щ": "Shch",
        "щ": "shch",
        "Ъ": "ie",
        "ъ": "ie",
        "Ы": "Y",
        "ы": "y",
        "Ь": "",
        "ь": "",
        "Э": "E",
        "э": "e",
        "Ю": "Iu",
        "ю": "iu",
        "Я": "Ia",
        "я": "ia",
    }
    result = ""
    for char in text:
        result += translit_dict.get(char, char)
    return result


@dp.message()
async def transliterate_name(message: Message):
    user_name = message.from_user.full_name
    user_id = message.from_user.id
    text = message.text
    if not text:
        await message.answer("Пожалуйста, отправь текст для транслитерации.")
        return
    if not re.fullmatch(r"[а-яёА-ЯЁ\s]+", text):
        await message.answer(
            "Пожалуйста, вводи только русские буквы без цифр и других символов."
        )
        return
    translit_text = transliterate(text)
    logging.info(f"{user_name} c id {user_id}: {text}. Ответ: {translit_text}")
    await message.answer(translit_text)


if __name__ == "__main__":
    dp.run_polling(bot)

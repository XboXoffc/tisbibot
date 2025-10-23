from bot import bot
from telebot import types
from utils.teacher_check import teacher_only
import config

DATA = config.DATA


@teacher_only
async def ask_homework_content(message:types.Message):
    user_id = message.from_user.id
    chat_id = message.chat.id
    subject = message.text.strip().lower()
    await bot.send_message(message.chat.id, f"✍️ Теперь введите домашнее задание по '{subject}':")
    async with bot.retrieve_data(user_id, chat_id) as data:
        data['subject'] = subject
    await bot.set_state(user_id, 'save_hw', chat_id)

@teacher_only
async def save_homework(message:types.Message):
    user_id = message.from_user.id
    chat_id = message.chat.id
    hw = message.text.strip()
    subject = None
    async with bot.retrieve_data(user_id, chat_id) as data:
        subject = data['subject']
    DATA["homework"][subject] = hw
    await bot.send_message(message.chat.id, f"✅ Домашнее задание по '{subject}' сохранено.")
    await bot.delete_state(user_id, chat_id)

async def get_homework_inline(message:types.Message):
    user_id = message.from_user.id
    chat_id = message.chat.id
    subject = message.text.strip().lower()
    hw = DATA["homework"].get(subject)
    await bot.send_message(message.chat.id, hw or f"❌ ДЗ по '{subject}' не найдено.")
    await bot.delete_state(user_id, chat_id)
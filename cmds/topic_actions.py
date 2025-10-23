from bot import bot
from telebot import types
from utils.teacher_check import teacher_only
import config

DATA = config.DATA


@teacher_only
async def ask_topic_content(message):
    user_id = message.from_user.id
    chat_id = message.chat.id
    subject = message.text.strip().lower()
    await bot.send_message(message.chat.id, f"📘 Теперь введите тему по '{subject}':")
    async with bot.retrieve_data(user_id, chat_id) as data:
        data['subject'] = subject
    await bot.set_state(user_id, 'save_topic', chat_id)

@teacher_only
async def save_topic(message):
    user_id = message.from_user.id
    chat_id = message.chat.id
    topic = message.text.strip()
    subject = None
    async with bot.retrieve_data(user_id, chat_id) as data:
        subject = data['subject']
    DATA["last_topic"][subject] = topic
    await bot.send_message(message.chat.id, f"✅ Тема по '{subject}' сохранена.")
    await bot.delete_state(user_id, chat_id)

async def get_topic_inline(message):
    user_id = message.from_user.id
    chat_id = message.chat.id
    subject = message.text.strip().lower()
    topic = DATA["last_topic"].get(subject)
    await bot.send_message(message.chat.id, topic or f"❌ Тема по '{subject}' не найдена.")
    await bot.delete_state(user_id, chat_id)
from bot import bot
from telebot import types
import config

DATA = config.DATA

async def main(call:types.CallbackQuery):
    user_id = call.from_user.id
    chat_id = call.message.chat.id
    if call.data == 'set_hw':
        await bot.send_message(call.message.chat.id, "✏️ Введите предмет, по которому хотите задать ДЗ:")
        await bot.set_state(user_id, 'ask_hw_content', chat_id)
    elif call.data == 'get_hw':
        await bot.send_message(call.message.chat.id, "📖 Введите предмет, чтобы получить ДЗ:")
        await bot.set_state(user_id, 'get_hw_inline', chat_id)
    elif call.data == 'set_topic':
        await bot.send_message(call.message.chat.id, "📝 Введите предмет, для которого хотите установить тему:")
        await bot.set_state(user_id, 'ask_topic_content', chat_id)
    elif call.data == 'get_topic':
        await bot.send_message(call.message.chat.id, "📚 Введите предмет, чтобы получить тему:")
        await bot.set_state(user_id, 'get_topic_inline', chat_id)
    elif call.data == 'list_subjects':
        subjects = set(DATA["homework"].keys()) | set(DATA["last_topic"].keys())
        text = "📚 Нет предметов." if not subjects else "📚 Предметы:\n" + "\n".join(sorted(subjects))
        await bot.send_message(call.message.chat.id, text)
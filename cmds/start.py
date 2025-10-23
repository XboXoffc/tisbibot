from bot import bot
from telebot import types

async def main(message:types.Message):
    markup = types.InlineKeyboardMarkup(row_width=2)
    buttons = [
        types.InlineKeyboardButton("📘 Установить ДЗ", callback_data='set_hw'),
        types.InlineKeyboardButton("📗 Получить ДЗ", callback_data='get_hw'),
        types.InlineKeyboardButton("📙 Установить тему", callback_data='set_topic'),
        types.InlineKeyboardButton("📒 Получить тему", callback_data='get_topic'),
        types.InlineKeyboardButton("📚 Список предметов", callback_data='list_subjects')
    ]
    markup.add(*buttons)  ###TODO добавить проверку на учителя, чтобы ученикам не показывались учительские кнопки
    await bot.send_message(message.chat.id, "👋 Привет! Выбери действие:", reply_markup=markup)
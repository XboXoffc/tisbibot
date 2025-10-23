from bot import bot
from telebot import types
import asyncio
import os
import config, tokens
from utils.teacher_check import teacher_only
from cmds import start, callback, hw_actions, topic_actions



TEACHER_IDS = config.TEACHER_IDS
ADMIN_IDS = config.ADMIN_IDS
DATA = config.DATA



@bot.message_handler(func=lambda message:True)
async def send_welcome(message:types.Message):
    user_id = message.from_user.id
    chat_id = message.chat.id
    state = await bot.get_state(user_id, chat_id)
    msgsplit = message.text.split(" ")
    
    if msgsplit[0] in ["/start", "/help"]:
        await start.main(message)
    elif state != None:
        if state == 'ask_hw_content':
            await hw_actions.ask_homework_content(message)
        elif state == 'save_hw':
            await hw_actions.save_homework(message)
        elif state == 'get_hw_inline':
            await hw_actions.get_homework_inline(message)
        elif state == 'ask_topic_content':
            await topic_actions.ask_topic_content(message)
        elif state == 'save_topic':
            await topic_actions.save_topic(message)
        elif state == 'get_topic_inline':
            await topic_actions.get_topic_inline(message)



@bot.callback_query_handler(func=lambda call: True)
async def callback_handler(call):
    await callback.main(call)


print("бот запущен\n\n\n")
asyncio.run(bot.infinity_polling())
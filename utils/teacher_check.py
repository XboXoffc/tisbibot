import config 

TEACHER_IDS = config.TEACHER_IDS

def teacher_only(func):
    async def wrapper(message):
        if message.from_user.id in TEACHER_IDS:
            return await func(message)
        else:
            await bot.reply_to(message, "Ты не учитель брооо")
    return wrapper
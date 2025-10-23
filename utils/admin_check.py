import config

ADMIN_IDS = config.ADMIN_IDS
TEACHER_IDS = config.TEACHER_IDS

async def is_admin(user_id):
    return user_id in ADMIN_IDS or user_id in TEACHER_IDS
def admin_only(func):
    async def wrapper(message):
        if await is_admin(message.from_user.id):
            return await func(message)
        else:
            await bot.reply_to(message, "У тебя нет прав администратора.")
    return wrapper
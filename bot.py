from telebot.async_telebot import AsyncTeleBot
from telebot.asyncio_storage import StateMemoryStorage
from telebot.asyncio_filters import StateFilter
import tokens

bot = AsyncTeleBot(tokens.TG, state_storage=StateMemoryStorage())
bot.add_custom_filter(StateFilter(bot))


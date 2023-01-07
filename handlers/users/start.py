from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from keyboards.default.locat import button
from loader import dp, bot
from data.config import ADMINS
from aiogram.utils.markdown import hlink




@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f"Salom, {message.from_user.full_name}!")
    await bot.send_message(chat_id=message.from_user.id, text="Menga joylashuv manzilingizni yuboring\nMen sizga eng yaqin Metro bekati haqida malumot beraman", reply_markup=button)

    
    msg = hlink(message.from_user.full_name, f'tg://openmessage?user_id={message.chat.id}')
    await bot.send_message(chat_id=ADMINS[0], text=msg)

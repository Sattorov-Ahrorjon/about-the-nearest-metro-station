from aiogram.types import KeyboardButton, ReplyKeyboardMarkup


button = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Location",request_location=True)
        ]
    ],
    resize_keyboard=True
)
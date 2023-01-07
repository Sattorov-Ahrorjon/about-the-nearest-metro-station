from aiogram import types
from loader import dp
from utils.misc.get_distance import choose_shortest


@dp.message_handler(content_types=types.ContentTypes.LOCATION)
async def get_answer(message: types.Message):
    try:
        
        location = message.location
        lat = location.latitude
        lon = location.longitude
        closest_shops = choose_shortest(location=location)
        text = "\n\n".join([f"<a href='{url}'>{shop_name}</a>\nMasofa: {distance:.1f} km."
                            for shop_name, distance, url, shop_location in closest_shops])
        
        txt = f"Rahmat .\nLatitude {lat}\nLongitude {lon}\n\n{text}"
        await message.answer(text, disable_web_page_preview=True)
        
        for shop_name, distance, url, shop_location in closest_shops:
            await message.answer_location(latitude=shop_location["lat"], longitude=shop_location["lon"])
    except:
        await message.reply("Joylashuv malumotida xatolik bor !")

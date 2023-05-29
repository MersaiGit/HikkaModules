# meta developer: @Mersai
from telethon.tl.types import Message
from .. import loader, utils

@loader.tds
class YandexPic(loader.Module):
    """Ищет картинку из Яндекса по вашему запросу."""

    strings = {"name": "YandexPic"}

    @loader.unrestricted
    async def yanscmd(self, message: Message):
        """запрос"""
        text = utils.get_args_raw(message)
        if not text:
            await message.edit("❌ Не указан запрос")
            return
        text_with_plus = text.replace(" ", "+")
        link = f"https://yandex.uz/images/touch/search/?text={text_with_plus}"
        try:
            await self.inline.form(
                message=message,
                text=f"🔍 Ваше фото по запросу \"{text}\" найдено",
                reply_markup=[
                    [
                        {
                            "text": "Photo link",
                            "url": link,
                        }
                    ],
                    [{"text": "Close", "action": "close"}],
                ],
                **({"photo": link}),
            )
        except:
            await message.edit(f"❌ Не удалось найти картинку по запросу \"{text}\".")
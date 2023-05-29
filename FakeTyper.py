# meta developer: @Mersai
from asyncio import sleep
from telethon import functions
from .. import loader, utils

@loader.tds
class FakeTypeMod(loader.Module):
    """Фейк тайпер"""

    strings = {"name": "FakeTypeMod"}

    async def typercmd(self, message):
        """время в секундах, для отключения .restart"""
        args = utils.get_args(message)
        if args:
            try:
                await message.respond('')
                async with message.client.action(message.chat_id, "typing"):
                    await sleep(int(args[0]))
            except ValueError:
                await message.edit("Некорректное значение времени.")
            except:
                pass
        else:
            await message.edit("Укажите время тайпа в секундах.")
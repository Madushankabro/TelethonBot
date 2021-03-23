# @DamienSoukara

from .. import BotzHub
from telethon import events, Button

@Alty.on(events.NewMessage(incoming=True, pattern="/start"))
async def start(event):
    await event.reply("Hello!",
                    buttons=[
                        [Button.url("ButtonUrl", url="https://t.me/DamienSoukara")],
                        [Button.inline("Inline Button",data="example")]
                    ])

@Alty.on(events.callbackquery.CallbackQuery(data="example"))
async def ex(event):
    await event.edit("You clicked a button!")

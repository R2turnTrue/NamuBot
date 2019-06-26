import discord
import asyncio
from itertools import cycle

client = discord.Client()

statusmsg = ['namu!help를 입력하세요!','나무봇 개발중!']

@client.event
async def on_ready():
    print(client.user.id)
    print("ready")

async def change_status():
    await client.wait_until_ready()
    messages = cycle(statusmsg)

    while not client.is_closed():
        current_status = next(messages)
        game = discord.Game(current_status)
        await client.change_presence(status=discord.Status.online,activity=game)
        await asyncio.sleep(4)

@client.event
async def on_message(message):
    if message.content.startswith("namu!help"):
        embed = discord.Embed(
            title="도움말",
            description="나무봇 도움말 입니다.",
            color=discord.Colour.green()
        )
        embed.add_field(name="명령어",value="namu!help\nnamu!hi\nnamu!status\nnamu!ping\nnamu!beep")
        await message.channel.send(embed=embed)

client.loop.create_task(change_status())
client.run("비밀")

import discord

client = discord.Client();
Token = 'ODgzMzc4MTAzNjM4OTYyMjU2.YTJD-A.6lmBAZzWQ98o6Ve9cXWkEEuxp6g'

@client.event
async def on_ready():
    print("Active.")

@client.event
async def on_message(message):
    if message.author.bot:
        return
    await message.channel.send('Hello')

client.run(Token)
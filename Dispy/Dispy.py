import discord

client = discord.Client();
Token = ''

@client.event
async def on_ready():
    print("Active.")

@client.event
async def on_message(message):
    if message.author.bot:
        return

client.run(Token)
import os
import random
from dotenv import load_dotenv
from discord.ext import commands
import requests

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='!')


@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')


@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    content = message.content
    if content in ['F', 'f']:
        response = f'{message.author} has paid respects.'
        await message.channel.send(response)

    else:
        res = requests.post('http://127.0.0.1:5000/infer', data={'sentence': content})
        is_sarcastic = res.json()['prediction']
        if is_sarcastic:
            await message.channel.send('That was a probably sarcasm.')

    await bot.process_commands(message)


@bot.command(name='s', help='Responds with an insult')
async def insult(ctx):
    insults = [
        'Eat it.',
        'Shut up!',
        'Any askers?'
    ]

    response = random.choice(insults)
    await ctx.send(response)


bot.run(TOKEN)

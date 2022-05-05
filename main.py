from discord.ext import commands
import  discord
from python_aternos import Client
import scrape
import MeCab

token = "OTUyMTk1MTc4MDYyNTY1NDE4.GGvF9g.YSyrogUaPDrD5KlU9qdi3TAAcVD3pn7b9Up16A"
intents = discord.Intents.all()

bot = commands.Bot(intents=intents,command_prefix='/')

@bot.event
async def on_message(message):
    if message.author.bot:
        return
    wakati = MeCab.Tagger("-Owakati")
    words = wakati.parse(message.content).split()
    if 'ねる' in words:
        await message.channel.send('寝るほうのねる')

bot.run(token)

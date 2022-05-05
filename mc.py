from python_aternos import Client

from discord.ext import commands
import discord

class MCserver(commands.Cog):
    
    def __init__(self,bot):
        self.bot = bot
        self.username = 'hyugois'
        self.password = 'hyugo1116'

    def start_server(self):
        aternos = Client(self.username,password=self.password)
        servs = aternos.list_servers()
        mcsv = servs[0]

        mcsv.start()
        return mcsv.address

    
    @commands.command
    async def start(self,ctx):
        address = self.start_server()
        embed = discord.Embed(title='サーバーを起動中です',description=f'`{address}`',color=discord.Colour.from_rgb(0,255,127))
        embed.add_field(name='**起動に失敗したら**',value='`既にサーバーがオンライン説`',inline=False)
        embed.set_footer(text='今度時間あったらサーバーの状態を確認できるやつも作るから俺に免じて許してね',icon_url='https://cdn.discordapp.com/attachments/768438484427735041/960876271934525450/IMG_1966.png')

        await ctx.message.reply(embed)

def setup(bot):
    bot.add_cog(MCserver(bot))
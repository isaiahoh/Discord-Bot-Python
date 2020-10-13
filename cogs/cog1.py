import discord
from discord.ext import commands

class cog1(commands.Cog): #inherit from commands.Cog basically a Class

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('Bot is online. ')
    
    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f'Pong!')

def setup(client):
    client.add_cog(cog1(client))
    

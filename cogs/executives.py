import discord
from discord.ext import commands

class Executives(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def clear(self, ctx, amount = 5):
        await ctx.channel.purge(limit = amount)

    #kick
    #asterick is so that multiple strings are added to reason variable
    @commands.command()
    async def kick(self, ctx, member : discord.Member, *, reason = None):
        await member.kick(reason=reason)

    #bans users
    @commands.command()
    async def ban(self, ctx, member : discord.Member, *, reason = None):
        await member.ban(reason=reason)
        await ctx.send(f'Banned{member.mention}')

    #unbans user
    @commands.command()
    async def unban(self, ctx, *, member):
        banned_users = await ctx.guild.bans()
        member_name, member_discriminator = member.split('#')

        for ban_entry in banned_users:
            user = ban_entry.user

            if(user.name, user.discriminator) == (member_name, member_discriminator):
                await ctx.guild.unban(user)
                await ctx.send(f'Unbanned {user.name}#{user.discriminator}')
                return

def setup(client):
    client.add_cog(Executives(client))

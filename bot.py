#start with: pip install discord.py in cmd

#importing libraries
import discord
from discord.utils import get
import os
from discord.ext import commands

#adding prefix to bot commands
client = commands.Bot(command_prefix = '.')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
#Computer Chapter    
    if message.content.startswith('join computer chapter'):
        member = message.author
        role = get(member.guild.roles, name='Computer Chapter')
        await member.add_roles(role, reason = None)

    if message.content.startswith('leave computer chapter'):
        member = message.author
        role = get(member.guild.roles, name='Computer Chapter')
        await member.remove_roles(role, reason = None)
#EMBS Chapter        
    if message.content.startswith('join embs chapter'):
        member = message.author
        role = get(member.guild.roles, name='EMBS Chapter')
        await member.add_roles(role, reason = None)

    if message.content.startswith('leave embs chapter'):
        member = message.author
        role = get(member.guild.roles, name='EMBS Chapter')
        await member.remove_roles(role, reason = None)
#discord committee
    if message.content.startswith('join discord committee'):
        member = message.author
        role = get(member.guild.roles, name='Discord Committee')
        await member.add_roles(role, reason = None)

    if message.content.startswith('leave discord committee'):
        member = message.author
        role = get(member.guild.roles, name='Discord Committee')
        await member.remove_roles(role, reason = None)
#workshop
    if message.content.startswith('join workshop committee'):
        member = message.author
        role = get(member.guild.roles, name='Workshop Committee')
        await member.add_roles(role, reason = None)

    if message.content.startswith('leave workshop committee'):
        member = message.author
        role = get(member.guild.roles, name='Workshop Committee')
        await member.remove_roles(role, reason = None)
#Website
    if message.content.startswith('join website committee'):
        member = message.author
        role = get(member.guild.roles, name='Website Committee')
        await member.add_roles(role, reason = None)

    if message.content.startswith('leave website committee'):
        member = message.author
        role = get(member.guild.roles, name='Website Committee')
        await member.remove_roles(role, reason = None)
#Public Relations
    if message.content.startswith('join public relations committee'):
        member = message.author
        role = get(member.guild.roles, name='Public Relations Committee')
        await member.add_roles(role, reason = None)

    if message.content.startswith('leave public relations committee'):
        member = message.author
        role = get(member.guild.roles, name='Public Relations Committee')
        await member.remove_roles(role, reason = None)
#Social
    if message.content.startswith('join social committee'):
        member = message.author
        role = get(member.guild.roles, name='Social Committee')
        await member.add_roles(role, reason = None)

    if message.content.startswith('leave social committee'):
        member = message.author
        role = get(member.guild.roles, name='Social Committee')
        await member.remove_roles(role, reason = None)
    await client.process_commands(message)



#COMMANDS

@client.command()
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')
    print(f'{extension} successfully loaded')

@client.command()
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')
    print(f'{extension} successfully unloaded')


#loading all the cog files
for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')
        
    
#input your bot token into the parentheses get from bot tab
client.run('NzYzOTAxMjQyNjAyNDIyMzAy.X3-ceA.xkT9T3-HkRoH0JFACIO7KgjPiro')





    

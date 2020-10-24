import discord
import re
import checkNewShoes

from discord.ext import commands
from discord.utils import get

TOKEN = 'TOKEN'
PREFIX = '.'

bot = commands.Bot(command_prefix = PREFIX)

@bot.event
async def on_ready():
	print(f'{bot.user.name} is ready.')

@bot.event
async def on_member_join(member : discord.Member):
	print(f'{member} has joined a server.')

@bot.command()
async def hi(ctx, role : discord.Role=None):
	print('hi')


bot.run(TOKEN)
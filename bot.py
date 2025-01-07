import discord
from discord.ext import commands
import asyncio
import random

# Bot 初始化
intents = discord.Intents.default()  
intents.messages = True  # 启用消息相关事件（根据需求启用特定事件）
intents.message_content = True
intents.emojis =True
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.command()
@commands.has_permissions(administrator = True) # 擁有管理員權限才能使用
async def synccommand(ctx):
    await bot.tree.sync()
    await ctx.send("同步完成")

@bot.hybrid_command()
async def test(ctx, url: str):
    await ctx.send("測試正常")



# 讀取TOKEN
f = open('TOKEN.txt', 'r')
TOKEN = f.read()
f.close()

bot.run(TOKEN)

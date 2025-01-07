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
async def test(ctx):
    await ctx.send("測試正常")

@bot.hybrid_command()
async def cast_moon_blocks(ctx, question: str):
    """
        Parameters:
        question (str): 要問的問題
    """
    await ctx.send(question)
    ans = random.choice(["正 正", "正 反", "反 正", "正 正"])
    await ctx.send(ans)



@bot.hybrid_command()
async def dice(ctx, dice: int, face : int):
    """
        Parameters:
        dice (int): 骰子數量
        face (int): 骰子有幾面
    """
    reply = ""
    sum = 0
    num = 0
    for i in dice:
        num = random.randint(1, face)
        reply = reply + str(num) + " "
        sum = sum + num
    await ctx.send(reply + "總共" + str(sum))



# 讀取TOKEN
f = open('TOKEN.txt', 'r')
TOKEN = f.read()
f.close()

bot.run(TOKEN)

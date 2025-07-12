import discord
from discord.ext import commands
import asyncio
import random
import os
from datetime import date
import time

import threading
from flask import Flask

# Flask 是為了讓Render不會因為沒有PORT而停止
# 建立一個 Flask 應用
app = Flask(__name__)

@app.route("/")
def home():
    return "Hello! This is a placeholder web server for a Discord bot."

# 啟動 HTTP 服務的函數
def run():
    port = os.getenv("PORT", 10000)  # 使用 Render 提供的 PORT 環境變數
    print("port is: " + port + "\n\n\n")
    app.run(host="0.0.0.0", port=port)

# 在獨立執行緒中運行 HTTP 服務
threading.Thread(target = run).start()

# Bot 初始化
intents = discord.Intents.default()  
intents.messages = True 
intents.message_content = True
intents.emojis =True
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.command()
@commands.has_permissions(administrator = True) # 擁有管理員權限才能使用
async def synccommand(ctx):
    await bot.tree.sync()
    await ctx.send("同步完成") # 要同步才能讓hybird command能夠使用

@bot.hybrid_command()
async def test(ctx):
    """
    測試
    """
    await ctx.send("測試正常")

@bot.hybrid_command()
async def cast_moon_blocks(ctx, question: str):
    """
        question (str): 要問的問題
    """
    await ctx.send(question)
    ans = random.choice(["聖杯", "聖杯", "笑杯", "陰杯"])
    await ctx.send(ans)

@bot.hybrid_command()
async def dice(ctx, dice: int, face : int):
    """
        dice (int): 骰子數量 face (int): 骰子有幾面
    """
    reply = ""
    sum = 0
    num = 0
    for i in range(dice):
        num = random.randint(1, face)
        reply = reply + str(num) + ","
        sum = sum + num
    await ctx.send(reply + "點數總共" + str(sum))

@bot.hybrid_command()
async def fortune(ctx):
    today = str(date.today())
    user_id = str(ctx.author.id)
    seed = today + user_id
    random_seed = random.Random(seed) # 固定同一天會是同一個結果
    print(seed)
    return_str = random_seed.choice(["大吉", "吉", "小吉", "大凶", "凶", "小凶"])
    return_str = today + ":" + return_str
    await ctx.send(return_str)

@bot.hybrid_command()
async def choice(ctx, Options:str):
    """
        Options (str): 選項用空白隔開
    """
    Option = Options.split()
    ans = random.choice(Option)
    await ctx.send(ans)

try:
    # 讀取TOKEN
    f = open('TOKEN.txt', 'r') # 如果資料夾有TOKEN.txt就讀取他並獲得TOKEN
    TOKEN = f.read()
    f.close()
except:
    TOKEN = os.getenv("TOKEN") # 否則嘗試讀取環境變數的TOKEN
time.sleep(5)  # 延遲 5 秒再連線
print("Token starts with:", TOKEN[:10]) 
bot.run(TOKEN)




import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

# .env を読み込む（※Koyebでは Environment variables が使われる）
load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

# intents 設定（必須）
intents = discord.Intents.default()
intents.message_content = True

# Bot 作成（★ここが重要）
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"ログイン完了: {bot.user}")

@bot.command()
async def 生成(ctx):
    await ctx.send("<:green_portion:1444959334550208564>")

# Bot 起動
bot.run(TOKEN)

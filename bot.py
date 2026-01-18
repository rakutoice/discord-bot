import os
import asyncio
import discord
from discord.ext import commands
from dotenv import load_dotenv
from aiohttp import web

# ===== 環境変数 =====
load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

# ===== Discord Bot =====
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"ログイン完了: {bot.user}")

@bot.command()
async def 生成(ctx):
    await ctx.send("<:green_portion:1444959334550208564>")

# ===== ダミーWebサーバー（Koyeb対策）=====
async def handle(request):
    return web.Response(text="Bot is running")

async def start_webserver():
    app = web.Application()
    app.router.add_get("/", handle)

    runner = web.AppRunner(app)
    await runner.setup()

    port = int(os.environ.get("PORT", 8000))
    site = web.TCPSite(runner, "0.0.0.0", port)
    await site.start()

# ===== 並列起動 =====
async def main():
    await start_webserver()
    await bot.start(TOKEN)

asyncio.run(main())

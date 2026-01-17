from discord.ext import commands
from aiohttp import web
import asyncio
import os

bot = commands.Bot(command_prefix="!")

async def healthcheck(request):
    return web.Response(text="OK")

async def start_web_server():
    app = web.Application()
    app.router.add_get("/", healthcheck)
    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, "0.0.0.0", 8000)
    await site.start()
    print("Healthcheck server running")

@bot.event
async def on_ready():
    print(f"ログイン完了: {bot.user}")

async def main():
    await start_web_server()
    await bot.start(os.environ["DISCORD_TOKEN"])

asyncio.run(main())

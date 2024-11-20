import discord
from discord.ext import commands
from dotenv import load_dotenv
import os
import ssl
import certifi
from aiohttp import ClientSession, TCPConnector

from database import initialize_database
from commands import handle_add_task, handle_delete_task, handle_show_tasks, handle_complete_task

# Load environment variables
load_dotenv()
TOKEN = os.getenv("DISCORD_BOT_TOKEN")

# Initialize bot with intents
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

# Global variables for aiohttp session
session = None

# Initialize database
@bot.event
async def on_ready():
    global session
    ssl_context = ssl.create_default_context(cafile=certifi.where())
    session = ClientSession(connector=TCPConnector(ssl=ssl_context))
    initialize_database()
    print(f"Bot berhasil login sebagai {bot.user}")

# Command: Add task
@bot.command()
async def add_task(ctx, *, description):
    await handle_add_task(ctx.message, description)

# Command: Delete task
@bot.command()
async def delete_task(ctx, task_id: int):
    await handle_delete_task(ctx.message, task_id)

# Command: Show tasks
@bot.command()
async def show_tasks(ctx):
    await handle_show_tasks(ctx.message)

# Command: Complete task
@bot.command()
async def complete_task(ctx, task_id: int):
    await handle_complete_task(ctx.message, task_id)

# Clean up the aiohttp session on shutdown
@bot.event
async def on_disconnect():
    global session
    if session and not session.closed:
        await session.close()

@bot.command()
async def ping(ctx):
    print("Ping command received")
    await ctx.send("Pong!")

# Run the bot
bot.run(TOKEN)

import discord
from discord.ext import commands, tasks
import asyncio

# 🔐 Fill in your actual details here
TOKEN = "3e5d581ccf5e909f37d3306a54dde74dbbe34b00711bff046d7c3ed858feb437"  # 🔁 Use your NEW bot token here
CHANNEL_ID = 1378746612934901840 # 🔁 Replace with your actual Discord channel ID

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"✅ Logged in as {bot.user}")
    self_ping.start()

@tasks.loop(minutes=3)
async def self_ping():
    channel = bot.get_channel(CHANNEL_ID)
    if channel:
        msg = await channel.send("🔁 Self-ping to stay awake.")
        print("[PING] Sent and will delete.")
        await asyncio.sleep(1)
        await msg.delete()

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    msg = message.content.lower()

    if msg in ["hi", "hello"]:
        await message.channel.send(f"Hello {message.author.mention}!")

    await bot.process_commands(message)

@bot.command()
async def hi(ctx):
    await ctx.send(f"Hi there, {ctx.author.mention}!")

bot.run(TOKEN)

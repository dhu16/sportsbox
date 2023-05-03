import discord
import os
from getnews import getNBANews, getNFLNews
from gettiktokstuff import getnbalinks, getnfllinks
from gettodayscores import getScores
from discord.ext import commands
from dotenv import load_dotenv


load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

# client = discord.Client(intents=discord.Intents.default())

# @client.event
# async def on_ready():
# print(f'{client.user} has connected to Discord!')

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)


@bot.command(name='nbanews')
async def nbanews(ctx):  # pragma: no cover
    """!nbanews - Posts NBA news articles to Discord"""
    articles = getNBANews()

    embed = discord.Embed(title="NBA Recent News")

    for a in articles:
        desc = a.description + "  [Read]({})".format(a.link)
        embed.add_field(name=a.headline, value=desc, inline=False)

    await ctx.send(embed=embed)


@bot.command(name='nflnews')
async def nflnews(ctx):  # pragma: no cover
    """!nflnews - Posts NFL news articles to Discord"""
    articles = getNFLNews()

    embed = discord.Embed(title="NFL Recent News")

    for a in articles:
        desc = a.description + "  [Read]({})".format(a.link)
        embed.add_field(name=a.headline, value=desc, inline=False)

    await ctx.send(embed=embed)


@bot.command(name='nbascores')
async def nbascores(ctx):  # pragma: no cover
    """!nbascores - Posts today's NBA box scores"""
    games = getScores()

    embed = discord.Embed(title="NBA Box Scores")

    for g in games:
        score = g.awayTeam + " " + str(g.aScore) + "    @    " + str(g.hScore) + " " + g.homeTeam
        embed.add_field(name=score, value=g.gameStatusText, inline=False)

    await ctx.send(embed=embed)


@bot.command(name='nbavids')
async def nbavids(ctx):  # pragma: no cover
    await ctx.send("Loading...")

    vids = await getnbalinks()

    embed = discord.Embed(title="Latest NBA Highlights")

    for link, caption in vids.items():
        desc = "[Watch]({})".format(link)
        embed.add_field(name=caption, value=desc, inline=False)

    await ctx.send(embed=embed)


@bot.command(name='nflvids')
async def nflvids(ctx):  # pragma: no cover
    await ctx.send("Loading...")

    vids = await getnfllinks()

    embed = discord.Embed(title="Latest NFL Highlights")

    for link, caption in vids.items():
        desc = "[Watch]({})".format(link)
        embed.add_field(name=caption, value=desc, inline=False)

    await ctx.send(embed=embed)


@bot.command(name='dogger')
async def dogger(ctx):  # pragma: no cover
    embed = discord.Embed(title="Dogger of the Month")

    file = discord.File("dogger/dogger.png", filename="image.png")
    embed.set_image(url="attachment://image.png")
    await ctx.send(file=file, embed=embed)


# client.run(TOKEN)
bot.run(TOKEN)

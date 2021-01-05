import discord
from discord.ext import commands
import os, requests, json

bot = commands.Bot(command_prefix='$')

@bot.event
async def on_ready():
  print('Logged in as ' + str(bot.user.name) + '#' + str(bot.user.discriminator) + '(' + str(bot.user.id) + ')')
    
@bot.command(name='ez',description='gg no re',category="funni")
async def _bot(ctx):
  await ctx.send("https://tenor.com/view/ez-yann-gauthier-gif-18979624")

@bot.command(name='quote',description='Get Inspired!',category="funni",aliases=['inspire'])
async def quote(ctx):
  def random():
    response = requests.get("https://zenquotes.io/api/random")
    json_data = json.loads(response.text)
    quote = json_data[0]['q'] + " - " + json_data[0]['a']
    return(quote)
  quote = random()
  embed = discord.Embed(
    title=quote
  )
  await ctx.send(embed=embed)

@bot.command(name='derg',description='Nice doggy!',category="funni",aliases=['dog'])
async def derg(ctx):
  embed = discord.Embed(
    title="░▄▀▄▀▀▀▀▄▀▄░░░░░░░░░\n░█░░░░░░░░▀▄░░░░░░▄░\n█░░▀░░▀░░░░░▀▄▄░░█░█\n█░▄░█▀░▄░░░░░░░▀▀░░█\n█░░▀▀▀▀░░░░░░░░░░░░█\n█░░░░░░░░░░░░░░░░░░█\n█░░░░░░░░░░░░░░░░░░█\n░█░░▄▄░░▄▄▄▄░░▄▄░░█░\n░█░▄▀█░▄▀░░█░▄▀█░▄▀░\n░░▀░░░▀░░░░░▀░░░▀░░░"
  )
  await ctx.send(embed=embed)

bot.run(os.getenv('BOT_TOKEN'))
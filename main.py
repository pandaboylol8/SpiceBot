import discord
from discord.ext import commands
import os, requests, json

def random_quote():
  response = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quote = json_data[0]['q'] + " - " + json_data[0]['a']
  return(quote)

bot = commands.Bot(command_prefix='$')

@bot.event
async def on_ready():
  print('Logged in as ' + str(bot.user.name) + '#' + str(bot.user.discriminator) + '(' + str(bot.user.id) + ')')

@bot.command(name='quote',description='Get Inspired!',aliases=['inspire'])
async def quote(ctx):
  quote = random_quote()
  embed = discord.Embed(
    title=quote
  )
  await ctx.send(embed=embed)

@bot.command(name='ez',description='gg no re')
async def _bot(ctx):
  await ctx.send("https://tenor.com/view/ez-yann-gauthier-gif-18979624")
  
@bot.command(name='gummi',description='🐻🐻🐻🐻 🧟 👉😗👈 🌪',aliases=['gummy'])
async def _bot(ctx):
  await ctx.send("https://vm.tiktok.com/ZMJWJQCSH/")

@bot.command(name='derg',description='Nice doggy!',aliases=['dog'])
async def derg(ctx):
  embed = discord.Embed(
    title="░▄▀▄▀▀▀▀▄▀▄░░░░░░░░░\n░█░░░░░░░░▀▄░░░░░░▄░\n█░░▀░░▀░░░░░▀▄▄░░█░█\n█░▄░█▀░▄░░░░░░░▀▀░░█\n█░░▀▀▀▀░░░░░░░░░░░░█\n█░░░░░░░░░░░░░░░░░░█\n█░░░░░░░░░░░░░░░░░░█\n░█░░▄▄░░▄▄▄▄░░▄▄░░█░\n░█░▄▀█░▄▀░░█░▄▀█░▄▀░\n░░▀░░░▀░░░░░▀░░░▀░░░"
  )
  await ctx.send(embed=embed)

bot.run(os.getenv('BOT_TOKEN'))
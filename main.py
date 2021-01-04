import discord
import os
import requests
import json

client = discord.Client()

def get_quote():
  response = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quote = json_data[0]['q'] + " - " + json_data[0]['a']
  return(quote)


@client.event

async def on_ready():
  print ('bot has logged in as {0.user}'.format(client))



@client.event
async def on_message(message):
  if message.author == client.user:
    return


  if message.content.startswith('$hello'):
    await message.channel.send('Hello, ya like spices??')

  
  if message.content.startswith('$pp'):
    await message.channel.send('Why do you have to get so political??')

  if message.content.startswith('https://tenor.com/view/ok-okay-awkward-smile-gif-5307535'):
    await message.channel.send('Ok.')

  if message.content.startswith('https://tenor.com/view/cat-gif-19827448'):
    await message.channel.send('SOOOO CUTTTTE')

  if message.content.startswith('$ez'):
    await message.channel.send('https://tenor.com/view/ez-yann-gauthier-gif-18979624')

  if message.content.startswith('$fortnite'):  
    await message.channel.send('ur bad')

  if message.content.startswith('$inspire'):
    quote = get_quote()
    await message.channel.send (quote)
  
  if message.content.startswith('$help'):
    await message.channel.send('$hello, $pp, $ez, $fortnite, $inspire(the best one, save for last)')
client.run(os.getenv('TOKEN'))
import discord
import pandas as pd

client = discord.Client()
guild = discord.Guild

def readPrevMessage():
	channels = client.get_all_channels();

	for c in channels:
		for m in c.messages(limit=200):
			print(m)

@client.event

async def on_message(message):
	if message.author == client.user: # in case of discord bot
		return

	# we're going to have it read everything
	# we'll need another if here for your user
	message1 = message.content;
	author1 = message.author;
	channel = message.channel;
	time = message.created_at


	if message.content.startswith('dasamoodreg'):
		username = message.content.split()[0].replace("dasamoodreg","")
		username = message.content.split()[1:][0]
		print(username)
		readPrevMessage();
		
		await channel.send(username)



	print(message1)
	print(author1)
	print(channel)
	print(time)
	print("")

client.run('');

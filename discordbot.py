import discord
from discord.ext import commands, tasks
import requests
from datetime import datetime
import json
from discord.ext import tasks

client = discord.Client()
guild = discord.Guild
botToken = "Nzk5ODUwNjE2OTI2NTAyOTYz.YAJk7w.0w_hR4hZMUWZgNcbhHFW9Vxr0BM"
filename = "lastcheck.txt"


@tasks.loop(seconds = 60*60)
async def getMessages():
	author = "";
	with open(filename, "r+") as f:
		prevTime = f.read()

		f.seek(0) 
		f.write(str(datetime.now())) # writing new datetime to file 
		f.truncate()
	
	jsonData = {} #json data to send
	jsonData['user'] = author

	jsonData['messages'] = []
	for c in channels: # Set to json
		async for msg in c.history(limit = 1000):
			if author = msg.author:
				jsonData['messages'].append({
					'messages': msg.content,
					'date': msg.created_at.date(),
					'time': msg.created_at.time()
				})
	with open('post.txt', 'w') as outfile:
		json.dump(jsonData, outfile)


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


	if message.content.startswith('dasamoodAllMessage'): # command to read all previous messages
		author = message.author #check with person who sent command
		channels = client.get_all_channels()

		with open(filename, "r+") as f:
			data = f.read()
			f.seek(0) 
			f.write(str(datetime.now())) # writing new datetime to file 
			f.truncate()
		
		jsonData = {} #json data to send
		jsonData['user'] = author

		jsonData['messages'] = []
		for c in channels: # Set to json
			async for msg in c.history():
				if author = msg.author:
					jsonData['messages'].append({
						'messages': msg.content,
						'date': msg.created_at.date(),
						'time': msg.created_at.time()
					})
		with open('post.txt', 'w') as outfile:
    		json.dump(jsonData, outfile)

	#print(message1)
	#print(author1)
	#print(channel)
	#print(time)
	#print("")

client.run('Nzk5ODUwNjE2OTI2NTAyOTYz.YAJk7w.0w_hR4hZMUWZgNcbhHFW9Vxr0BM');

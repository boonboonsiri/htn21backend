import discord
from discord.ext import commands, tasks
import requests
from datetime import datetime, timedelta
import json
from discord.ext import tasks
import os

client = discord.Client()
guild = discord.Guild
botToken = "Nzk5ODUwNjE2OTI2NTAyOTYz.YAJk7w.0w_hR4hZMUWZgNcbhHFW9Vxr0BM"
filename = ".\lastcheck.txt.txt"
url = "http://127.0.0.1:8000/api/createmessage"
authorLoop = "";



async def getMessages():
	while True:
		print("HELLO WORLD");
		print(os.getcwd())
		prevTime = ""
		with open(filename, "r+") as f:
			prevTime = f.read()
			prevTime = datetime.strptime(prevTime, '%Y-%m-%d %H:%M:%S.%f')
			f.seek(0) 
			f.write(str(datetime.now())) # writing new datetime to file 
			f.truncate()
			f.close()
		#jsonData = {} #json data to send
		#jsonData['user'] = author
		#jsonData['messages'] = []
		for c in channels: # Set to json
			async for msg in c.history(limit = 1000):
				if authorLoop == msg.author and msg.create_at.date() > prevTime:
					jsonData = {
						'messages' : msg.content,
						'date' : str(msg.created_at.date()),
						'score' : str(0),
						'user' : "boon1",
						'time' : (msg.created_at.time() - timedelta(hours=5)).strftime("%H:%M:%S")
					} #json data to send
					requests.post(url,data = jsonData)
		await asyncio.sleep(5)
					#jsonData['messages'].append({
					#	'messages': msg.content,
					#	'date': msg.created_at.date(),
					#	'time': msg.created_at.time()
					#})
		#with open('post.txt', 'w') as outfile:
			#json.dump(jsonData, outfile)



#@client.event
#async def on_ready():
#    client.loop.create_task(getMessages())


@client.event
async def on_message(message):
	if message.author == client.user: # in case of discord bot
		return

	# we're going to have it read everything
	# we'll need another if here for your user
	#message1 = message.content;
	author1 = message.author;
	print(author1);
	#channel = message.channel;
	#time = message.created_at

	if message.content.startswith('dasamoodAllMessage'): # command to read all previous messages
		print("HERE")
		author = message.author #check with person who sent command
		channels = client.get_all_channels()
		#with open(filename, "r+") as f:
		#	data = f.read()
		#	f.seek(0) 
		#	f.write(str(datetime.now())) # writing new datetime to file 
		#	f.truncate()
		#	f.close()
		
		#jsonData['user'] = author
		for c in channels: # Set to json
			print(str(type(c)))
			if str(type(c)) != '<class \'discord.channel.CategoryChannel\'>' and str(type(c)) != '<class \'discord.channel.VoiceChannel\'>' and str(type(c)) != '<class \'discord.channel.VideoChannel\'>' :
				async for msg in c.history():
					if author == msg.author:
						jsonData = {
							'messages' : msg.content,
							'date' : str(msg.created_at.date()),
							'score' : str(0),
							'user' : "boon1",
							'time' : (msg.created_at.time() - timedelta(hours=5)).strftime("%H:%M:%S")

						} #json data to send
						x=requests.post(url,data = jsonData)
						print(x)
			#with open('post.txt', 'w') as outfile:
				#json.dump(jsonData, outfile)

	if message.content.startswith('dasamoodtest'):
		jsonData = {
			'messages' : message.content,
			'date' : str(message.created_at.date()),
			'score' : str(0),
			'user' : "boon",
			'time' : message.created_at.time().strftime("%H:%M:%S")
		} #json data to send
		x=requests.post(url,data = jsonData)
		print(x)



	#print(message1)
	#print(author1)
	#print(channel)
	#print(time)
	#print("")

client.run('Nzk5ODUwNjE2OTI2NTAyOTYz.YAJk7w.JPXIc0zEpVn9MkR6M9Wii6JFw5Y');

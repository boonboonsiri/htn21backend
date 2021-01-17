import discord
from discord.ext import commands, tasks
import requests
from datetime import datetime
import json
from discord.ext import tasks

url = "http://127.0.0.1:8000/api/createmessage"
#jsonData = {} #json data to send
##jsonData['Messages'] = "Hello"
##jsonData['Date'] = str(datetime.now().date)
#jsonData['Score'] = str(0)
#jsonData['User'] = "TestUser"
#jsonData['Time'] = "00:31:00"

jsonData = {
    'messages' : "hello5000",
    'date' : str(datetime.now().date()),
    'score' : str(0),
    'user' : "testuser",
    'time' : datetime.now().time().strftime("%H:%M:%S")
}

#{"messages":"Hello World 1","date":"2010-11-02","score":"0.00","user":"testuser","time":"00:31:00"}
x=requests.post(url, json = json.dumps(jsonData))
y=requests.post(url, data = jsonData)
print(json.dumps(jsonData))
print(jsonData)
print(x)
print(y)
import nextcord, time, asyncio, datetime, sys, os, random, os.path
from nextcord.ext import commands 
from os.path import exists
from nextcord import FFmpegPCMAudio, Interaction, SlashOption, ChannelType
from datetime import datetime
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.cron import CronTrigger
from pathlib import Path

file_exists = os.path.exists("tokenAndAppID.txt")

intents = nextcord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)
bot.remove_command('help')
token = 0
botID = 0
yesNo = 0

if(token == 0 and botID == 0 and (file_exists == True)):
    while yesNo not in ["yes","no"]:
        yesNo = input("you have a token and app id saved, do you want to use it [yes/no]: ")
        print("")    
if(yesNo == "yes"):
    file = open("tokenAndAppID.txt")
    content = file.readlines()
    print("token is "+ content[0])
    print("appID is "+ content[1])
    token = content[0]
    botID = content[1]
    print("")

elif(yesNo == "no", (token == 0) and (botID == 0) or file_exists == False):
    token = input("Enter your Discord Bot Token: ")
    print("")
    botID = input("Enter your Discord Bot App ID: ")
    print("")    
    with open("tokenAndAppID.txt", 'w') as a:
        a.write(token+"\n")
        a.write(botID)

print("ok wait 5 minutes for bot to load commmands and here is link to add to server also make sure it is a community server")
print("https://discord.com/api/oauth2/authorize?client_id=" + botID + "&permissions=8&scope=bot\n")
print("")
print("keep this window open till it tells you to close it")
print("")

@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))

@bot.slash_command(description="GIVE ME THE DISCORD ACTIVE DEVELOPER BADGE")
async def balls(interaction: nextcord.Interaction): 
    await interaction.response.send_message("because you wanted it here https://discord.com/developers/active-developer, if you dont see then wait a few minutes, hours or days")
    print("")
    print("wowowoo you got the 'probaly' discord active developer badge, you can now close this window")

bot.run(token)
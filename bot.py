import discord,asyncio,youtube_dl
from discord.ext import commands
import os
from dotenv import load_dotenv

load_dotenv()




def get_prefix(bot, msg):
    """A callable Prefix for our bot. This could be edited to allow per server prefixes."""

    prefixes = ['*'] #Your bot prefix(s)

    return commands.when_mentioned_or(*prefixes)(bot, msg)

"""bot=commands.Bot(command_prefix=get_prefix,description='Multipurpose Discord Bot')"""

"""client=commands.Bot(command_prefix=get_prefix,description='tasoeurlatepu',intents=intents)"""

intents = discord.Intents.all()
intents.message_content = True
intents.members = True
client = commands.Bot(command_prefix=get_prefix, intents=intents)
Bot = commands.Bot(command_prefix=get_prefix, intents=intents)



exts=['music'] #Add your Cog extensions here


@client.event
async def on_ready():
    song_name='TWICE - What is love?'  #Status name
    activity_type=discord.ActivityType.listening #Status type
    await client.change_presence(activity=discord.Activity(type=activity_type,name=song_name))
    print(client.user.name)






for i in exts:
    Bot.load_extension(i)


Bot.run(os.environ['TOKEN'])

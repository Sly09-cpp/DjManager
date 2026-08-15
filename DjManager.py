import discord
from discord.ext import commands
import asyncio

class DjManager:
    def __init__(self, token):
        self.__token__ = token
        
        # Initialize bot
        intents = discord.Intents.default()
        intents.message_content = True
        intents.voice_states = True
        self.__agent__ = commands.Bot(command_prefix='!', intents=intents)

        self.__voice_clients__ = {} # List of voice channels DJ has joined in a specific server


    def __register_commands__(self):
        @self.__agent__.command(name='join')
        async def join(ctx):
            if ctx.author.voice:
                channel = ctx.author.voice.channel
                vc_client = await channel.connect()
                self.__voice_clients__[ctx.guild.id] = vc_client
            else:
                await ctx.send("Join a voice channel to summon me.")
        
        @self.__agent__.command(name='play')
        async def play(ctx):
            
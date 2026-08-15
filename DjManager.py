import discord
import yt_dlp
from discord.ext import commands
import asyncio
import os
class DjManager:
    def __init__(self, token):
        self.__token__ = token
        
        # Initialize bot
        intents = discord.Intents.default()
        intents.message_content = True
        intents.voice_states = True
        self.__agent__ = commands.Bot(command_prefix='!', intents=intents)

        self.__voice_clients__ = {} # List of voice channels DJ has joined in a specific server
        self.__register_commands__()
        self.__agent__.run(self.__token__)

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
            if ctx.guild.id not in self.__voice_clients__:
                await join(ctx)

            vc_client = self.__voice_clients__[ctx.guild.id]

            # Options for yt-dlp to extract audio only
            ydl_opts = {
                'format': 'bestaudio/best',
                'postprocessors': [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'wav', # We convert to wav then pipe to opus
                    'preferredquality': '192',
                }],
                'quiet': True,
                'no_warnings': True,
            }

            try:
                await ctx.send(f"Searching for: {query}...")
                
                # Extract info without downloading to disk (streaming)
                with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                    info = ydl.extract_info(f"ytsearch1:{query}", download=False)
                    url = info['entries'][0]['url']
                    title = info['entries'][0]['title']
                    
                    await ctx.send(f"Now playing: {title}")

                    # Create the audio source
                    # discord.FFmpegPCMAudio handles the conversion to Opus internally
                    source = discord.FFmpegPCMAudio(url, before_options='-nostats')
                    
                    # Play the audio
                    if not vc_client.is_playing():
                        vc_client.play(source, after=lambda e: print(f'Error: {e}' if e else 'Track finished'))
                    else:
                        await ctx.send("Already playing something.")

            except Exception as e:
                await ctx.send(f"An error occurred: {str(e)}")

        @self.__agent__.command(name='leave')
        async def leave(ctx):
            if ctx.guild.id in self.__voice_clients__:
                await self.__voice_clients__[ctx.guild.id].disconnect()
                del self.__voice_clients__[ctx.guild.id]
                await ctx.send("Disconnected.")
            else:
                await ctx.send("I'm not connected.")
            
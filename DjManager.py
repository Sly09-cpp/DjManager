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
                    source = discord.FFmpegPCMAudio(url, before_options='-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', options='-bufsize 1024k')
                    
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

        @self.__agent__.command(name='pause')
        async def pause(ctx):
            if ctx.guild.id in self.__voice_clients__:
                vc_client = self.__voice_clients__[ctx.guild.id]
                if vc_client.is_playing():
                    vc_client.pause()
                    await ctx.send("Paused.")
                elif vc_client.is_paused():
                    await ctx.send("Song is already paused. Do **!resume** to continue playing or **!skip** to stop playing.")
                else:
                    await ctx.send("Oak: 'This isn't the time to use that!'")
            else:
                await ctx.send("Oak's words echoed... 'There's a time and place for everything but not now!'")
        
        @self.__agent__.command(name='resume')
        async def resume(ctx):
            if ctx.guild.id in self.__voice_clients__:
                vc_client = self.__voice_clients__[ctx.guild.id]
                if vc_client.is_paused():
                    vc_client.resume()
                    await ctx.send("Resumed.")
                elif vc_client.is_playing():
                    await ctx.send("Song is already playing. Do **!pause** to pause the song or **!skip** to stop playing.")
                else:
                    await ctx.send("Oak: 'This isn't the time to use that!'")
            else:
                await ctx.send("Oak's words echoed... 'There's a time and place for everything but not now!'")
    
            
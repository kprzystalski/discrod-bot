from gtts import gTTS
from discord.ext import commands
import discord
from pydub import AudioSegment

TOKEN = ""

bot = commands.Bot(command_prefix = "!")

@bot.command(name='dajglos',pass_context=True)
async def dajglos(ctx):
    print("Daje głos")
    tts = gTTS('Dobrze ', lang='pl', slow=False)
    tts.save('dobrze.mp3')
    sound = AudioSegment.from_mp3("dobrze.mp3")
    sound.export("dobrze.mp3")
    user=ctx.message.author
    voice_channel=user.voice.channel
    if voice_channel!= None:
        channel=voice_channel.name
        await ctx.send('Użytkownik na kanale: '+ channel)
        channel=voice_channel
        vc = await channel.connect()
        vc.play(discord.FFmpegPCMAudio('dobrze.mp3'), after= lambda e: print("Odtworzyłem"))
        while vc.is_playing():
            None
        vc.stop()
        await vc.disconnect()
    else:
        await ctx.send("Nie ma go na kanale")

bot.run(TOKEN)
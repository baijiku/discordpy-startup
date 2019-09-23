import discord
from datetime import datetime, timedelta

TOKEN = "NjI1NTA0NjgyMzkwODQ3NDk4.XYhbGA.4Au1O_jje4dsZ77KK31DQ84QwQM"
SEVER_ID = 625297697850785798
TEXT_CHANNEL = 625569697441644545

client = discord.Client()

@client.event
async def on_voice_state_update(member, before, after): 
    if member.guild.id == SEVER_ID and (before.channel != after.channel):
        now = datetime.utcnow() + timedelta(hours=9)
        alert_channel = client.get_channel(TEXT_CHANNEL)
        if before.channel is None: 
            msg = f'{now:%m/%d-%H:%M} に {member.name} が {after.channel.name} に参加しました。'
            await alert_channel.send(msg)
        elif after.channel is None: 
            msg = f'{now:%m/%d-%H:%M} に {member.name} が {before.channel.name} から退出しました。'
            await alert_channel.send(msg)

client.run(TOKEN)
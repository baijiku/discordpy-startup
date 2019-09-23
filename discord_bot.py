import discord
from datetime import datetime, timedelta

client = discord.Client()

@client.event
async def on_voice_state_update(member, before, after): 
    if member.guild.id == 625297697850785798 and (before.channel != after.channel):
        now = datetime.utcnow() + timedelta(hours=9)
        alert_channel = client.get_channel(625297697850785800)
        if before.channel is None: 
            msg = f'{now:%m/%d-%H:%M} に {member.name} が {after.channel.name} に参加しました。'
            await alert_channel.send(msg)
        elif after.channel is None: 
            msg = f'{now:%m/%d-%H:%M} に {member.name} が {before.channel.name} から退出しました。'
            await alert_channel.send(msg)

client.run("NjI1NTA0NjgyMzkwODQ3NDk4.XYg5fQ.RT35Mu4yYKsprt7tMkikl_subHE")
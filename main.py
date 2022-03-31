"""
https://discord.py.readthedocs.io/en/latest/intents.html
https://discord.com/developers/docs/topics/gateway#gateway-intents
https://discord.com/developers/docs/topics/gateway#list-of-intents
"""

import discord
import os

from keep_alive import keep_alive
keep_alive()

class MyClient(discord.Client):
  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.target_message_id = 958959832797433886
  
  async def on_ready(self):
    print('We have logged in as {0.user}'.format(client))
  
  # Add roles
  async def on_raw_reaction_add(self, payload):
    if payload.message_id != self.target_message_id:
      return

    guild = client.get_guild(payload.guild_id)

    if payload.emoji.name =='🌐':
      role = discord.utils.get(guild.roles, name='Portfolio Website Viewer')
      await payload.member.add_roles(role)
    elif payload.emoji.name== '🤖':
      role = discord.utils.get(guild.roles, name='Spu.D Bot Viewer')
      await payload.member.add_roles(role)
    elif payload.emoji.name == '📁':
      role = discord.utils.get(guild.roles, name='Potato Pack Viewer')
      await payload.member.add_roles(role)
  
  # Remove roles
  async def on_raw_reaction_remove(self, payload):
    if payload.message_id != self.target_message_id:
      return

    guild = client.get_guild(payload.guild_id)
    member = guild.get_member(payload.user_id)

    if payload.emoji.name =='🌐':
      role = discord.utils.get(guild.roles, name='Portfolio Website Viewer')
      await member.remove_roles(role)
    elif payload.emoji.name== '🤖':
      role = discord.utils.get(guild.roles, name='Spu.D Bot Viewer')
      await member.remove_roles(role)
    elif payload.emoji.name == '📁':
      role = discord.utils.get(guild.roles, name='Potato Pack Viewer')
      await member.remove_roles(role)

intents = discord.Intents.default()
intents.members = True

client = MyClient(intents=intents)
token = os.environ['TOKEN']

client.run(token)
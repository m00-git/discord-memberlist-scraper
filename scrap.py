#!/usr/bin/env python

import discord
from discord.ext import commands

TOKEN_AUTH = "TOKENHERE"

client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as '+client.user.name+'')

@commands.command()
async def getallmembers(self, ctx):
 print("\n===", ctx.guild.name, "===")
 print("Dumping all members to file...")
 with open(ctx.guild.name+"_members.txt", "w") as f:
   users = '\n'.join(str(user) for user in ctx.guild.members)
   f.write(users)

client.add_command(getallmembers) #or some shit idk

client.run(TOKEN_AUTH, bot=False)

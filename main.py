import discord
from discord.ext import commands, tasks
import random
from itertools import cycle


client = commands.Bot(command_prefix = '.')
status = cycle(['Minecraft Bedrock Edition', 'Uncountable♾Infinity'])

@client.event
async def on_ready():
	change_status.start()
	print('Discord Bot Online')

@tasks.loop(seconds=10)
async def change_status():
	await client.change_presence(activity=discord.Game(next(status)))

@client.command()
async def ping(ctx):
	await ctx.send(f'Pong! `{round(client.latency * 1000)}ms`')

@client.command(aliases=['8ball', 'test'])
async def _8ball(ctx, *, question):
	responses = ['It is certain',
					'It is decidedly so',
					'Without a doubt',
					'Yes – definitely',
					'You may rely on it',
					'As I see it, yes',
					'Most likely',
					'Outlook good',
					'Yes Signs point to yes',
					'Reply hazy',
					'try again',
					'Ask again later',
					'Better not tell you now',
					'Cannot predict now',
					'Concentrate and ask again',
					'Dont count on it',
					'My reply is no',
					'My sources say no',
					'Outlook not so good',
					'Very doubtful']
	await ctx.send(f'Question: {question}\nAnswer: {random.choice(responses)}')

@client.command()
async def clear(ctx, amount=6):
	await ctx.channel.purge(limit=amount)

@client.command()
async def kick(ctx, member : discord.Member, *, reason=None):
	await member.kick(reason=reason)
	await ctx.send(f'Kicked {member.mention}!')

@client.command()
async def ban(ctx, member : discord.Member, *, reason=None):
	await member.ban(reason=reason)
	await ctx.send(f'Banned {member.mention}!')

@client.command()
async def unban(ctx, *, member):
	banned_users = await ctx.guild.bans()
	member_name, member_discriminator = member.split('#')

	for banned_entry in banned_users:
		user = ban_entry.user

		if (user.name, user.discriminator) == (member_name, member_discriminator):
			await ctx.guild.unban(user)
			await ctx.send(f'Unbanned {member.mention}!')
			return


client.run('ODc4NDU0Mjk0NzMzNTUzNzA0.YSBaUA.akW4p5Gef-_pBMWhBlPBx8DHSYo')

import discord
from discord.ext import commands, tasks

intents = discord.Intents.default()
intents.members = True

token = 'OTQ2MDE5NzI4OTQwNDkwNzg1.YhYnhw.7CovgV_wOwj10sm3Fa_WKFqkai4'


bot = commands.Bot(command_prefix='-->', intents=intents) 

@bot.event
async def on_ready():
    print('bot is ready')

@bot.command()
@commands.has_permissions(administrator=True)
async def dm(ctx, user_id=None, *, args=None):
    if user_id != None and args != None:
        try:
            target= await bot.fetch_user(user_id)
            await target.send(args)
            await ctx.channel.send(f'sent to {target.name}')
        except:
            await ctx.channel.send(f'coudnt send to {target.name}')
    else:
        await ctx.channel.send('not included')


bot.run(token)
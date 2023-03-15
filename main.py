from decouple import config
import discord
from discord import app_commands
import pandas as pd

intents = discord.Intents.default()
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)


@tree.command(name="help", description="My first application Command", guild=discord.Object(id=config('GUILD_ID')))
async def help_command(interaction):
    response = 'Here are the available commands:\n\n/help - Shows a list of available commands\n'
    await interaction.response.send_message(response)


@client.event
async def on_ready():
    await tree.sync(guild=discord.Object(id=config('GUILD_ID')))
    print("Ready!")

    # Get channel
    df = pd.read_json('channels-static.json', dtype={'id': str})
    channel_id = str(df.loc[df['key'] == 'kimida-test', 'id'].values[0])
    channel = await client.fetch_channel(channel_id)

    # Send message to channel
    if channel is not None:
        await channel.send('Hello World!')
    else:
        print('Unable to find channel')


@client.event
async def on_message(message: discord.Message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

    if str(message.author.id) == config('KIMIDA_ID'):
        await message.channel.send('Miaou!')
        reaction = '🐱'
        await message.add_reaction(reaction)


client.run(config('TOKEN'))

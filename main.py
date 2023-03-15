from decouple import config
import discord
from discord import app_commands

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

    await client.process_commands(message)


client.run(config('TOKEN'))

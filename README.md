# Discord Bot Template in Python

This is a minimal architecture for building a discord bot using discord.py

## Examples

This template provides :
- A message sending in a text channel.
- A command builder with two examples (/help, /faq), and an Interaction listener.
- A way to react to messages

## Getting Started

### Define your Token, Client ID and Guild ID

Create an .env file at the root of your project and define your Discord bot token, Client ID and Guild ID in a variable as following:
```shell
TOKEN="Your_token_here"
CLIENT_ID="Your_client_id_here"
GUILD_ID="Your_guild_id_here"
```

### Define your channels

The channel IDs are defined in src/infra/channels-static.json
```json
[
    {
        "key": "custom_key",
        "id": "channel_id"
    }
]
```

### Install dependencies

```shell
pip3 install -r requirements.txt 
```

### Run

```shell
python3 main.py
```

## References

- [discord.py](https://discordpy.readthedocs.io/en/stable/): Python API wrapper for Discord.

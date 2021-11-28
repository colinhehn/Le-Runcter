import discord
from discord.ext import tasks, commands
import tweepy

# Le Runcter is a Twitter bot for reading specified accounts LIKED and POSTED tweets (including replies), and then posting them to a specified Discord channel.
# Originally designed for Intel's ARC Xe Scavenger Hunt.


# Twitter Auth Setup
auth = tweepy.OAuthHandler('S3UPGbuTjiKtjxNWM8VgWh2pU',
                           'clSlTmL5z4J0LbdlqLy5r3sBXUYWj8W6JUOSsq9cV5vDj0dmlf')
auth.set_access_token('831257102756757504-7EGUjdR3BT6l3r4AaLpeUz96Zw2TkoY',
                      'ILITaeHHQyLQdw6f9QyyuI97eIQKZdvNszW1qa10j3uP5')
api = tweepy.API(auth)


# Maintenance Variables
client = commands.Bot(command_prefix='!')
last_seen_id = '1465060366954770432'

# Bot Functionality - Checks Twitter for Likes every 5 Minutes, Posts to Discord
@tasks.loop(seconds=5.0)
async def check_favorites():
    global last_seen_id
    
    await client.wait_until_ready()
    channel = client.get_channel(914646418927538207)

    favorites = api.get_favorites(screen_name= 'colinhehn', since_id= last_seen_id)
    print(f'Grabbed {len(favorites)} favorites doe')
    
    if len(favorites) >= 1:
        print("CHECKING!!!!")
        id_list = []
        for favorite in favorites:
            await channel.send(f'{favorite.user.screen_name} at {favorite.id} - {favorite.text}')
            id_list.append(int(favorite.id))
            
        last_seen_id = max(id_list)
    else:
        print("No Favorites to Show!")

check_favorites.start()
client.run('OTA1MzIzMTQ0MTI5MTU1MDky.YYIZ4Q.Jp4WVmlZXIyhK25drK6Gflq8tcU')
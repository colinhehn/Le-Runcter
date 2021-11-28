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


# The Twitter Handles in Question
user_list = ['IntelGraphics', 'PGelSinger', 'RajaOnTheEdge', 'gfxLisa',
             'RogerDChandler', 'BobDuffy', 'CaptGeek', 'theBryceIsRt', 'XboxGamePassPC']


def retrieve_last_seen_id(file_name):
    f_read = open(file_name, 'r')
    last_seen_id = int(f_read.read().strip())
    f_read.close()
    return last_seen_id

def store_last_seen_id(last_seen_id, file_name):
    f_write = open(file_name, 'w')
    f_write.write(str(last_seen_id))
    f_write.close()
    return


# Maintenance Variables
client = commands.Bot(command_prefix='!')

# Bot Functionality - Checks Twitter for Likes every 5 Minutes, Posts to Discord
@tasks.loop(seconds=5.0)
async def check_favorites():
    
    await client.wait_until_ready()
    
    last_seen_id = retrieve_last_seen_id('last_seen_id.txt')
    
    channel = client.get_channel(913332196285222973)

    for user in user_list:
        favorites = api.get_favorites(screen_name=user, since_id=last_seen_id)
        if len(favorites) >= 1:
            print("CHECKING!!!!")
            for favorite in favorites:
                if favorite.id > int(last_seen_id):
                    store_last_seen_id(favorite.id, 'last_seen_id.txt')
                    await channel.send(f'{favorite.user.screen_name} at {favorite.created_at} - {favorite.text}')
        else: print("No Favorites to Show!")

check_favorites.start()
client.run('OTA1MzIzMTQ0MTI5MTU1MDky.YYIZ4Q.Jp4WVmlZXIyhK25drK6Gflq8tcU')

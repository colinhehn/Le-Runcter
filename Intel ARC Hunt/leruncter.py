from discord.ext import commands
import tweepy
import asyncio

# Le Runcter is a Twitter bot for reading specified accounts LIKED and POSTED tweets (including replies), and then posting them to a specified Discord channel.
# Originally designed for Intel's ARC Xe Scavenger Hunt.

# Need to host the app on Heroku, PythonAnywhere, Repl.it, or maybe GitHub?


# Twitter Auth Setup
auth = tweepy.OAuthHandler('S3UPGbuTjiKtjxNWM8VgWh2pU', 'clSlTmL5z4J0LbdlqLy5r3sBXUYWj8W6JUOSsq9cV5vDj0dmlf')
auth.set_access_token('831257102756757504-7EGUjdR3BT6l3r4AaLpeUz96Zw2TkoY', 'ILITaeHHQyLQdw6f9QyyuI97eIQKZdvNszW1qa10j3uP5')
api = tweepy.API(auth)

# The Twitter Handles in Question
user_list = ['IntelGraphics', 'PGelSinger', 'RajaOnTheEdge', 'gfxLisa', 'RogerDChandler', 'BobDuffy', 'CaptGeek', 'theBryceIsRt', 'XboxGamePassPC']

# Maintenance Variables
bot = commands.Bot(command_prefix='!')
last_seen_id = '1457479371757850628'

# Bot Functionality - Checks Twitter for Likes every 5 Minutes, Posts to Discord
async def check_favorites():
    await bot.wait_until_ready()
    channel = bot.get_channel(913332196285222973)
    
    for user in user_list:
        favorites = api.get_favorites(screen_name = user, since_id = last_seen_id)
        if favorites >= 1:
            for favorite in favorites:
                if favorite.id > last_seen_id: last_seen_id = favorite.id
                await channel.send('{} at {} - {}'.format(favorite.user.screen_name, favorite.created_at, favorite.text))
                
    await asyncio.sleep(300)

bot.loop.create_task(check_favorites())
bot.run('OTA1MzIzMTQ0MTI5MTU1MDky.YYIZ4Q.JBwCE-HSWPW-BMbOuXfvRdNHf4c')
    
    #print ('{} - {}'.format(chicken[0].id,chicken[0].text))
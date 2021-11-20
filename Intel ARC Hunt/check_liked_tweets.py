import tweepy
import time
import discord

client = discord.Client()



client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

#client.run('OTA1MzIzMTQ0MTI5MTU1MDky.YYIZ4Q.JBwCE-HSWPW-BMbOuXfvRdNHf4c')








# Le Runcter is a Twitter bot for reading specified accounts LIKED and POSTED tweets (including replies), and then posting them to a specified Discord channel.
# Originally designed for Intel's ARC Xe Scavenger Hunt.

# Need to host the app on Heroku, PythonAnywhere, Repl.it, or maybe GitHub?

auth = tweepy.OAuthHandler('S3UPGbuTjiKtjxNWM8VgWh2pU', 'clSlTmL5z4J0LbdlqLy5r3sBXUYWj8W6JUOSsq9cV5vDj0dmlf')
auth.set_access_token('831257102756757504-7EGUjdR3BT6l3r4AaLpeUz96Zw2TkoY', 'ILITaeHHQyLQdw6f9QyyuI97eIQKZdvNszW1qa10j3uP5')

api = tweepy.API(auth)


account_list = ['IntelGraphics', 'PGelSinger', 'RajaOnTheEdge', 'gfxLisa', 'RogerDChandler', 'BobDuffy', 'CaptGeek', 'theBryceIsRt', 'XboxGamePassPC']
last_seen_id = '1457479371757850628'
jack = '1128692733353218048'
# Function is called every time we want to see what tweets the designated users have liked since it was ran last.
def retrieve_liked_tweets():

    # need to have a separate "last_seen_id" for each account here OR get the last seen tweet's time of postage, find all tweets after that
    # ALSO, compile all of the tweets from every account into one tweet list, sort that list and find the latest one in that list, store that time of postage.
    ids = []
    pog = 1461873281678589958
    d = {}
    
    for tweeter in account_list:
        likes = []
        check = 0
        chicken = api.get_favorites(screen_name = tweeter, count = 1)
        d[tweeter] = chicken[0].id
        check+=1
    time.sleep(10)    
    return (d)
    
    #print ('{} - {}'.format(chicken[0].id,chicken[0].text)) 
    
        
        
# Once the liked tweets functionality is laid out,
# I could add a function showing all the tweets the users have posted,
# even though IFTTT does that right now.

# Automatic functionality within the script? Or do I want the Discord bot to do this instead?
# Might be faster to delegate the reoccurence of the script to the Discord bot.
#retrieve_liked_tweets()
client.event
async def on_ready():
    print(retrieve_liked_tweets())
client.run('OTA1MzIzMTQ0MTI5MTU1MDky.YYIZ4Q.JBwCE-HSWPW-BMbOuXfvRdNHf4c')
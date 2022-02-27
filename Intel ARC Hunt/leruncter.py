from discord.ext import tasks, commands
import tweepy


# Le Runcter is a Twitter bot for reading specified accounts LIKED and POSTED tweets (including replies), and then posting them to a specified Discord channel.
# Originally designed for Intel's ARC Xe Scavenger Hunt.


# Twitter Auth Setup
auth = tweepy.OAuthHandler('REDACTED',
                           'REDACTED')
auth.set_access_token('REDACTED',
                      'REDACTED')
api = tweepy.API(auth)


# The Twitter Handles in Question
user_list = ['IntelGraphics', 'PGelSinger', 'RajaOnTheEdge', 'gfxLisa',
             'RogerDChandler', 'BobDuffy', 'CaptGeek', 'theBryceIsRt', 'XboxGamePassPC']


# Function for retrieving and parsing the ID stored in last_seen_id.txt.
def retrieve_last_seen_id(file_name):
    f_read = open(file_name, 'r')
    last_seen_id = int(f_read.read().strip())
    f_read.close()
    print(f'Found last_seen_id! Value: {last_seen_id}')
    
    return last_seen_id


# Function for replacing the ID in last_seen_id.txt with a new one.
def store_last_seen_id(last_seen_id, file_name):
    f_write = open(file_name, 'w')
    f_write.write(str(last_seen_id))
    f_write.close()
    print(f'Wrote new last_seen_id! Value: {last_seen_id}')
    
    return


# Maintenance Variables
client = commands.Bot(command_prefix='!')


# Notification for when bot is live
@client.event
async def on_ready():
    print('Bot is logged in as {0.user} and running!'.format(client))


# Bot Functionality - Checks Twitter for Likes every 5 Minutes, Posts to Discord.
@tasks.loop(minutes=5.0)
async def check_favorites():
    
    await client.wait_until_ready()
    
    # Bot is bricking at this point. Must be an issue with client.wait_until_ready() or retrieve_last_seen_id().
    # Do some research!
    
    last_seen_id = retrieve_last_seen_id('last_seen_id.txt')
    print('last_seen_id retrieved.')
    
    channel = client.get_channel(REDACTED)
    print('Discord channel retrieved.')
    
    id_list = []
    favorite_list = []
    
    for user in user_list:
        
        favorites = api.get_favorites(screen_name=user, since_id=last_seen_id)
        print(f'List of favorites retrieved for {user}! Length: {len(favorites)}.')
        
        if len(favorites) >= 1:
            print(f'Favorites detected for {user}!')
            
            for favorite in reversed(favorites):
                    favorite_list.append(favorite)
                    id_list.append(int(favorite.id))
                    print(f'Favorite appended for {user}, ID appended: {favorite.id}')
                    
        else: print(f'No new favorites to show for {user}!')
    
    if len(favorite_list) >= 1:
        # sort favorite_list by favorite.created_at
        
        for favorite in favorite_list:
            await channel.send(f'{favorite.user.screen_name} at {favorite.created_at[0:9]} - {favorite.text}')
            print(f'Discord Message sent for {favorite.id}!')
    else: print('NO NEW FAVORITES FOR ALL USERS!')
        
    store_last_seen_id(max(id_list), 'last_seen_id.txt')
    print('New last_seen_id written to file.')


# Starting up the bot!
check_favorites.start()
print('Check favorites task started!')
client.run('REDACTED')

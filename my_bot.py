import os
import time
from markovbot import MarkovBot
tweetbot = MarkovBot()
dirname = os.path.dirname(os.path.abspath(__file__))
book = os.path.join(dirname, 'manifesto.txt')
tweetbot.read(book)
my_text = tweetbot.generate_text(25, seedword=['society', 'bourgeoisie'])
print(my_text)


# Consumer Key (API Key)
cons_key = 'TIShdZ9JgpYIyg8X4oJXAzgFq'
# Consumer Secret (API Secret)
cons_secret = 'qgLQKTadisYeb1T7DIVPNs17U7ce0LUaCAofHss8fiDWDMugpx'
# Access Token
access_token = '1087385094858387459-DijdGpPcFmugx0L86msnc5TOeXj8Gh'
# Access Token Secret
access_token_secret = 'XUAoW9ieporFcgqE1wMJnHEag4rpurUwJzewP7XCkhPgq'
#log in to twitter
tweetbot.twitter_login(cons_key, cons_secret, access_token, access_token_secret)
#set parameters for auto-replies
targetstring = "capitalism"
keywords = ['cultural', 'economics', 'proletariat', 'bourgeoisie']
prefix = None
suffix = None
maxconvdepth = 1
#start auto-replies
tweetbot.twitter_autoreply_start(targetstring, keywords=keywords, prefix=prefix, suffix=suffix, maxconvdepth=maxconvdepth)

# Start periodically tweeting
tweetbot.twitter_tweeting_start(days=0, hours=0, minutes=30, keywords=None, prefix=None, suffix='#communism')
# something has to happen here to let my bot be active
# You could, for example, wait for a week:
secsinweek = 7 * 24 * 60 * 60
time.sleep(secsinweek)

tweetbot.twitter_autoreply_stop()
tweetbot.twitter_tweeting_stop()


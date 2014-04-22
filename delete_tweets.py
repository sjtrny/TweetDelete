import tweepy
from tweepy.error import TweepError
import json
import glob
import dateutil.parser

api_key = 'XXXXXXXXXXXXXXXX'
api_secret = 'XXXXXXXXXXXXXXXX'

access_token = 'XXXXXXXXXXXXXXXX'
access_token_secret = 'XXXXXXXXXXXXXXXX'

file_dir = 'tweets/data/js/tweets'

date_min = dateutil.parser.parse('2009-01-01 00:00:00 +0000')
date_max = dateutil.parser.parse('2010-01-01 00:00:00 +0000')

print "Tweets between %s and %s will be deleted" % (date_min.isoformat(), date_max.isoformat())
print "Do you wish to continue? (y/n)"
choice = raw_input("> ")

if choice == 'y':
	auth = tweepy.OAuthHandler(api_key, api_secret)
	auth.set_access_token(access_token, access_token_secret)
	
	api = tweepy.API(auth)
	
	file_list = glob.glob(file_dir + '/*.js')
	file_list.sort()
	
	for file_name in file_list:
		print file_name
		f = open(file_name, 'r')
		f.readline() # clear the first junk line
		data = json.load(f);
		
		for tweet in data:
			tweet_date = dateutil.parser.parse(tweet['created_at'])
			if tweet_date > date_min and tweet_date < date_max:
				print "-----------------------------------"
				print "%s: %s" % (tweet['created_at'], tweet['text'])
				try:
					api.destroy_status(tweet['id'])
					print "DELETED"
				except TweepError as te:
					print "ERROR %s" % te[0][0]['message']
			else:
				break
else:
	print "No tweets deleted"

print "Goodbye!"
TweetDelete
===========

Python script to delete tweets within a date range.

Dependencies
-----------

- [tweepy](http://www.tweepy.org)
- json
- glob
- dateutil

User Guide
-----------

1. Download your [Twitter archive](https://twitter.com/settings/account)
- Install dependencies (usually only tweepy) e.g.`pip install tweepy`
- Make a developer account at [dev.twitter.com](http://dev.twitter.com)
- Create a new twitter app
- Set app permissions to read and write
- Generate access token for your account
- Set API and access key-secret pairs in `delete_tweets.py` i.e. `api_key`, `api_secret`, `access_token` and `access_token_secret`
- Set `file_dir` to point to directory containing JSON formatted tweets
- Set date range by adjusting`date_min` and `date_max`
- Run using `python delete_tweets.py`

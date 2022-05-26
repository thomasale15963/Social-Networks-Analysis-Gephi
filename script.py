import csv
import tweepy
import csv
import pandas as pd

# credentials for api
consumer_key = ''
consumer_secret = ''
access_token = ''
access_token_secret = ''


# authenticate session and create api instance
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, wait_on_rate_limit=True)

# init csv writter
csvFile = open('nodes-1.csv', 'a')
csvWriter = csv.writer(csvFile)


def process_info(screen_name, followers_count, tweet_count):
    # get people screen name
    for myFollowings in api.get_friends(screen_name=screen_name, count=followers_count):

        allCurrentScreenNameHashTags = []

        # get user info
        try:
            userJson = api.get_user(screen_name=screen_name)._json

            if(userJson['screen_name'] == 'ethiotelecom'):
                pass
            else:
                csvWriter.writerow([screen_name, myFollowings.screen_name])
                print(screen_name, ",", myFollowings.screen_name)
        except Exception as e:
            print(e)


with open('./data/NodeList.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        process_info(row[0], 40, 20)

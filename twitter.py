#!/usr/bin/env python
# encoding: utf-8
from textblob import TextBlob
import tweepy
import pandas as pd
import sys
#from nltk.sentiment.vader import SentimentIntensityAnalyzer

# declare the keys and secrets
consumer_key = "" 
consumer_secret = ""
access_key = ""
access_secret = ""

# authorize
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)

# initialize
twitter_api = tweepy.API(auth)

def sentiment_analyze(usr_input):
    # keyword and number of tweets
    keyword = usr_input[:-1]
    tweet_num = int(usr_input[-1])

    # get tweets
    tweets = tweepy.Cursor(twitter_api.search_tweets, q=keyword, lang="en").items(tweet_num)

    # analyze sentiment score
    tweet_list = []
    sentiment_score = []
    for tweet in tweets:
        tweet_list.append(tweet.text)
        #tweet_list.append(tweet._json)
        analysis = TextBlob(tweet.text)
        sentiment_score.append(analysis.sentiment.polarity)

    #output
    print(f"The sentiment score of the {keyword}: ")

    #print(tweet_list)
    #print sentence score
    total_score = 0
    i = len(sentiment_score)
    for sentence in range(0,len(sentiment_score)):
        total_score += sentiment_score[sentence]  
        if sentiment_score[sentence] == 0:
            i = i - 1
        print(f"Sentence {sentence} have a sentiment score of {sentiment_score[sentence]}")

    average_score = total_score / i

    print(f"The total sentiment score of the {keyword}is {total_score}")
    print(f"The average sentiment score of the {keyword}is {average_score}")

    if average_score > 0:
        print("nice product!")
        recommand = True
    else:
        print("not recommended product!")
        recommand = False
    return average_score, recommand

if __name__ == '__main__':
    usr_input = sys.argv[1:]
    average, recommand = sentiment_analyze(usr_input)

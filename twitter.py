# -*- coding: utf-8 -*-
"""
Created on Thu May 12 10:38:47 2016

@author: appertjt
"""

from TwitterSearch import*
import credentials
import pandas

tweet_file='C:\\Users\\appertjt\\Documents\\Python Scripts\\sentiment\\twitter.csv'
consumer_key=credentials.twitter_consumer_key
secret_key=credentials.twitter_consumer_secret
access_token=credentials.twitter_access_token
access_secret=credentials.twitter_token_secret

header=['text', 'favorite_count', 'retweet_count', 'created_at']
tweet_list=[]


######helper function######
def get_twt(keyword):
    try:
        x=tweet[keyword].encode('ascii', 'ignore')
    except:
        x='N/A'
    return x
    

try:
    tso=TwitterSearchOrder()
    tso.set_keywords(['Giants'])
    tso.set_language('en')
    tso.set_include_entities(False)
    tso.set_count(20)
    
    ts=TwitterSearch(consumer_key, secret_key, access_token, access_secret)


    for tweet in ts.search_tweets_iterable(tso):
        try:
            sub=[]
            sub.append(get_twt('text'))
            sub.append(get_twt('favorite_count'))
            sub.append(get_twt('retweet_count'))
            sub.append(get_twt('created_at'))
            sub.append(get_twt('id_str'))
            tweet_list.append(sub)

        except:
            pass

except TwitterSearchException as e:
    print(e)


pd=pandas.DataFrame(tweet_list)
pd.to_csv(tweet_file)

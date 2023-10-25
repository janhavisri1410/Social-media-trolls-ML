import csv
import tweepy
import ssl


def writeonfile(file_num,texts):
    file1 = open('myfile'+str(file_num)+'.txt', 'w')

    for i,line in enumerate(texts):
        file1.write(line)
        file1.write("\n")
    file1.close()

ssl._create_default_https_context = ssl._create_unverified_context
# Oauth keys
consumer_key = "HRIUnNTYa1ByO8XtrlVY0NJZG"
consumer_secret = "Ebf3OTfSJQMR8ABppDAq9anRPvIeGvLbsU7YWA4sfs6RtG8mY2"
access_token = "1384389462885494785-7gbbDAZqH4RLeC1EjbRBwzJYrPQ2jZ"
access_token_secret = "61884KsjoKaCh4QiEHpswIUhMz1XLDmCRvy0fMJgwVRn7"
# Authentication with Twitter
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)


# tweet_id = '763431264577728512'
texts = []
count= 0
file_num = 0
total_count = 0
fline_count=0
neg = open('Dataset/newdata/election-filter1.txt').read()
for i, line in enumerate(neg.split("\n")):
    tweet_id = line
    fline_count=fline_count +1
    try:
        tweet = api.get_status(tweet_id)
        if tweet.lang != "en":
            continue
        st = tweet.text
        texts.append(st)
        count=count+1
        total_count = total_count + 1
        if count == 10000:
            writeonfile(file_num,texts)
            file_num=file_num+1
            texts = []
            count = 0
        print(count,fline_count)
    except:
        continue

writeonfile(file_num,texts)
print(total_count)





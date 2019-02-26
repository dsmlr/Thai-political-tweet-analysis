import csv
import re
from pythainlp.sentiment import sentiment
import json

def remove_newline(tweet):
    return tweet.replace('\r\n', '').replace('\n', '')

def remove_hashtag(tweet):
    return re.sub(r'(\#[\u0E00-\u0E7Fa-zA-Z]+)', "", tweet)

def keep_only_thai(tweet):
    return re.sub(r'([^\u0E00-\u0E7F\s])', '', tweet)

def convert_multiple_space_to_single(tweet):
    return re.sub(r'\s{2,}', ' ', tweet)

def remove_start_space(tweet):
    return re.sub(r'^\s', '', tweet)


def main(party_name):
    unique_tweets = set()

    with open('csv/%s.csv' % party_name, encoding='utf8') as csvfile:
        data = csv.DictReader(csvfile, delimiter=';')

        for row in data:
            tweet = row['text']

            tweet = remove_newline(tweet)
            tweet = keep_only_thai(tweet)
            tweet = convert_multiple_space_to_single(tweet)
            tweet = remove_start_space(tweet)

            unique_tweets.add(tweet)

    count = {'pos': 0, 'neg': 0}
    for tweet in unique_tweets:
        count[sentiment(tweet, engine='old')] += 1
    
    return count


if __name__ == '__main__':
    for i in ['ประชาธิปัตย์', 'พลังประชารัฐ', 'รวมพลังประชาชาติไทย', 'เสรีรวมไทย', 'เพื่อไทย', 'อนาคตใหม่']:
        print(i, main(i))

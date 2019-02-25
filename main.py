from twitter_scraper import get_tweets
import json

PARTY_TW_ACCOUNTS = ['Thanathorn_FWP', 'sudaratofficial', 'Abhisit_DP', 'KPuvaphat', 'PprpBangkok']

def strip_newline(tweet):
    return tweet.replace('\r\n', ' ').replace('\n', ' ')

def main(party):
    data = ''

    for tweet in get_tweets(party, pages=10):
        striped_tweet = strip_newline(tweet['text'])

        data += striped_tweet + ' '

    print('Account: %s has %d tweets in this batch.' % (party, len(data)))

    with open('pure-text-%s.json' % party, 'w', encoding='utf8') as outfile:
        json.dump(data, outfile, ensure_ascii=False)


if __name__ == "__main__":
    for party in PARTY_TW_ACCOUNTS:
        main(party)


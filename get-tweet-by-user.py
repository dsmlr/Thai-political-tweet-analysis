import got3 as got
import json
import threading
import os
from time import sleep
import random

output_files = os.listdir('./user-tweet')

def main(user_list):
    for user in user_list:
        tweetCriteria = got.manager.TweetCriteria().setUsername(user).setSince('2019-02-18').setUntil('2019-02-24')
        tweets = got.manager.TweetManager.getTweets(tweetCriteria)

        with open('./user-tweet/%s.json' % user, 'w', encoding='utf8') as fp:
            data = []
            for tw in tweets:
                data.append({
                    'id': tw.id,
                    'url': tw.permalink,
                    'username': tw.username,
                    'text': tw.text,
                    'date': tw.date.strftime('%d-%m-%Y %H:%M'),
                    'retweet': tw.retweets,
                    'like': tw.favorites,
                })
            json.dump(data, fp, ensure_ascii=False)

        print('%s tweets has been saved.' % user)

if __name__ == "__main__":
    with open('username_list.txt', 'r') as fp:
        users = fp.readlines()

    print(len(set(users)), len(output_files))

    users = map(lambda x: x.strip(), users)
    users = filter(lambda x: '%s.json' % x not in output_files, users)
    users = list(users)

    print(len(users), len(output_files))

    random.shuffle(users)

    user_list1, user_list2 = users[:3110], users[3110:]
    thread1 = threading.Thread(target=main, args=(user_list1,))
    thread2 = threading.Thread(target=main, args=(user_list2,))

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()


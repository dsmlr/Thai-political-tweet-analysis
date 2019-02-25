import csv
import re
import json

def main(party_name):
    with open('week-tweets/%s.csv' % party_name, encoding='utf8') as csvfile:
        data = csv.DictReader(csvfile, delimiter=';')
        
        sum_rt, sum_fav = 0, 0
        most_rt_tweet, most_fav_tweet = {}, {}
        daily_rt = {'18': 0, '19': 0, '20': 0, '21': 0, '22': 0, '23': 0, '24': 0}
        daily_fav = {'18': 0, '19': 0, '20': 0, '21': 0, '22': 0, '23': 0, '24': 0}
        daily_tweet = {'18': 0, '19': 0, '20': 0, '21': 0, '22': 0, '23': 0, '24': 0}

        for row in data:
            sum_rt += int(row['retweets'])
            sum_fav += int(row['favorites'])

            if most_rt_tweet == {} or int(most_rt_tweet['retweets']) < int(row['retweets']):
                most_rt_tweet = row

            if most_fav_tweet == {} or int(most_fav_tweet['favorites']) < int(row['favorites']):
                most_fav_tweet = row
    
            day = row['date'][8:10]

            if int(day) < 25:
                daily_rt[day] += int(row['retweets'])
                daily_fav[day] += int(row['favorites'])
                daily_tweet[day] += 1

    csvfile.close()

    json_data = {
        "sum_rt": sum_rt,
        "sum_fav": sum_fav,
        "most_rt_tweet": {
            "id": most_rt_tweet['id'],
            "text": most_rt_tweet['text'],
            "rt": int(most_rt_tweet['retweets']),
            "fav": int(most_rt_tweet['favorites']),
        },
        "most_fav_tweet": {
            "id": most_fav_tweet['id'],
            "text": most_fav_tweet['text'],
            "rt": int(most_fav_tweet['retweets']),
            "fav": int(most_fav_tweet['favorites']),
        },
        "daily_rt": daily_rt,
        "daily_fav": daily_fav,
        "daily_tweet": daily_tweet
    }

    with open('tweet-analysis-%s.json' % party_name, 'w', encoding='utf8') as fp:
        json.dump(json_data, fp, ensure_ascii=False)

if __name__ == '__main__':
    for i in ['ประชาธิปัตย์', 'พลังประชารัฐ', 'รวมพลังประชาชาติไทย', 'เสรีรวมไทย', 'เพื่อไทย', 'อนาคตใหม่']:
        main(i)

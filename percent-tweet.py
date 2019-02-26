import json

party_name_list = ['ประชาธิปัตย์', 'พลังประชารัฐ', 'รวมพลังประชาชาติไทย', 'เสรีรวมไทย', 'เพื่อไทย', 'อนาคตใหม่']
sum_tweets = {'18': 2282, '19': 1313, '20': 2283, '21': 1727, '22': 1594, '23': 1467, '24': 813}

for party_name in party_name_list:
    with open('tweet-analysis-%s.json' % party_name, 'r', encoding='utf8') as fp:
        data = json.load(fp)

        for day in data['daily_tweet']:
            print(party_name, day, data['daily_tweet'][day])

print(sum_tweets)


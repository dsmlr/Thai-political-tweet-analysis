import csv

def main(party_name):
    url_tweets = []

    with open('./csv/%s.csv' % party_name, 'r', encoding='utf8') as fp:
        data = csv.DictReader(fp, delimiter=';')
    
        for row in data:
            url_tweets.append(row['permalink'])

    username = map(lambda url: None if url == None else url.split('/')[3], url_tweets)
    username = filter(lambda usr: usr != None, username)

    return list(set(username))
    

if __name__ == "__main__":
    users = []

    for ptn in ['ประชาธิปัตย์', 'พลังประชารัฐ', 'รวมพลังประชาชาติไทย', 'เสรีรวมไทย', 'เพื่อไทย', 'อนาคตใหม่']:
        users += main(ptn)

    with open('username_list.txt', 'w') as fp:
        fp.write('\n'.join(users))
    fp.close()
    

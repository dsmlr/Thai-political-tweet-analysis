from wordcloud import WordCloud
import matplotlib.pyplot as plt
import csv
import re
import pythainlp
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

    freq = {}
    for tweet in unique_tweets:
        for word in pythainlp.tokenize.word_tokenize(tweet,engine='deepcut'):
            striped = word.strip()
            for splited in striped.split():
                if freq.get(splited, None) == None:
                    freq[splited] = 1
                else:
                    freq[splited] += 1

    file = open('word-freq/%s.json' % party_name, 'w', encoding='utf8')
    json.dump(freq, file, ensure_ascii=False)
    file.close()


    # wc = WordCloud(
    #     font_path='Arundinamono.ttf',
    #     background_color="white",
    #     width=1024,
    #     height=768,
    #     regexp=r"[\u0E00-\u0E7Fa-zA-Z']+",).generate(wordline)

    # plt.imsave('%s.png' % party_name, wc)


if __name__ == '__main__':
    for i in ['ประชาธิปัตย์', 'พลังประชารัฐ', 'รวมพลังประชาชาติไทย', 'เสรีรวมไทย']:
        main(i)

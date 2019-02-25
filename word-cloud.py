import json
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from pythainlp.corpus import stopwords

def main(party_name):
    with open('word-freq/%s.json' % party_name, 'r', encoding='utf8') as fp:
        data = json.load(fp)

    wc = WordCloud(
        font_path='THSarabunNew.ttf',
        background_color="white",
        stopwords=stopwords.words('thai'),
        width=1024,
        height=768,
        margin=3,
        regexp=r"[\u0E00-\u0E7Fa-zA-Z']+").fit_words(data)

    plt.imsave('%s.png' % party_name, wc)

if __name__ == '__main__':
    for i in ['ประชาธิปัตย์', 'พลังประชารัฐ', 'รวมพลังประชาชาติไทย', 'เสรีรวมไทย', 'เพื่อไทย']:
        main(i)
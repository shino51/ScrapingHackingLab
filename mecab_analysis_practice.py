import MeCab
import requests
from bs4 import BeautifulSoup
from gensim.models import word2vec


def mecab_kakiwari_practice():
    url = "https://ja.wikipedia.org/wiki/Google_Pixel"
    m = MeCab.Tagger("-Owakati")
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    text = soup.find("p").get_text()
    parse_text = m.parse(text)
    print(parse_text)


def kakiwari_from_wikipedia():
    domain = "https://ja.wikipedia.org/wiki/"
    names = ["森鷗外", "夏目漱石", "島崎藤村",
             "与謝野晶子", "坪内逍遥", "石川啄木",
             "谷崎潤一郎", "芥川龍之介", "萩原朔太郎",
             "川端康成", "志賀直哉", "中原中也",
             "太宰治", "大岡昇平", "三島由紀夫"]
    m = MeCab.Tagger("-Owakati")
    corpus = []

    for name in names:
        with requests.get(domain + name) as response:
            soup = BeautifulSoup(response.content, "html.parser")
            p_text = soup.find_all("p")
            for p in p_text:
                corpus.append(m.parse(p.text).strip())

    with open("data.txt", "w", encoding="utf-8") as file:
        file.write("\n".join(corpus))


def analyse_data_after():
    file = open("data.txt", encoding="utf=8")
    corpus = file.read().splitlines()
    corpus = [sentence.split() for sentence in corpus]
    model = word2vec.Word2Vec(corpus, vector_size=200, min_count=20, window=20)
    model.save("data.model")
    similar_words = model.wv.most_similar(positive=["文学"], topn=9)
    print(*[" ".join([v, str("{:.2f}".format(s))]) for v, s in similar_words], sep="\n")


def analyse_existing_model():
    # read model from the existing data.model:
    model = word2vec.Word2Vec.load("data.model")
    similar_words = model.wv.most_similar(positive=["文学"], topn=9)
    print(*[" ".join([v, str("{:.2f}".format(s))]) for v, s in similar_words], sep="\n")


if __name__ == '__main__':
    kakiwari_from_wikipedia()
    analyse_data_after()

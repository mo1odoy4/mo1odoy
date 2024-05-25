from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem.snowball import SnowballStemmer
import pymorphy3

with open("../tokenstasks/txt.txt", encoding="utf-8") as f:
    text = f.read()


def clean_text(text: str):
    clean_text = "".join(el for el in text if el.isalpha() or el.isspace())
    with open("clean_text.txt", "w", encoding="utf-8") as clean:
        clean.write(clean_text)
    return clean_text


def not_stop_words(clean: str):
    tokens = word_tokenize(clean)
    stop_words = stopwords.words("russian")
    texts = " ".join(el for el in tokens if el.lower() not in stop_words)
    with open("not_stop_words.txt", "w", encoding="utf-8") as stop:
        stop.write(texts)
    return texts


def super_stem(text: str):
    stemmer = SnowballStemmer("russian")
    tokens = word_tokenize(text)
    stemmed_words = ' '.join(stemmer.stem(word) for word in tokens)
    with open("super_stem.txt", "w", encoding="utf-8") as stop:
        stop.write(stemmed_words)
    return stemmed_words


def super_lemm(text: str):
    morph = pymorphy3.MorphAnalyzer(lang="ru")
    tokens = word_tokenize(text)
    lemme_words = ' '.join(morph.parse(token)[0].normal_form for token in tokens)
    with open("super_lemm.txt", "w", encoding="utf-8") as o:
        o.write(lemme_words)
    return lemme_words


p = clean_text(text)
a = not_stop_words(clean=p)
super_stem(text=a)
super_lemm(text=a)

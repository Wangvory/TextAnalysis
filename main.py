# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import os
import nltk
from nltk.corpus import brown
from nltk.corpus import wordnet as wn
from nltk.corpus import PlaintextCorpusReader
from nltk.probability import FreqDist
from nltk.text import Text
from nltk.corpus import stopwords
os.getcwd()

## Reading source data
def read_text(path):
    if os.path.isdir(path):
        raw=PlaintextCorpusReader(path, '.*').raw()
        tokens = nltk.tokenize.word_tokenize(raw)
    else:
        f = open(path)
        raw=f.read()
        tokens = nltk.tokenize.word_tokenize(raw)
        
    return Text(tokens)


## Generate simple statistics
def token_count(text):
    count=len(text)
    return count


def type_count(text):
    raw = set(text)
    ty=len(raw)
    return ty

def sentence_count(text):
    re_string=' '.join(text)
    numsent = nltk.tokenize.sent_tokenize(re_string)
    count=len(numsent)
    return count

def most_frequent_content_words(text):
    text_clean = [word for word in text if word.strip(',.<>?!;:\'"|`~@#$%^&*()-[]{}+-——=').isalpha()]
    stopword = nltk.corpus.stopwords.words('english')
    content = [w for w in text_clean if w.lower() not in stopword]
    fdist = FreqDist(content)
    return fdist.most_common(25)


def most_frequent_bigrams(text):
    text_clean = [word for word in text if word.strip(',.<>?!;:\'"|`~@#$%^&*()-[]{}+-——=').isalpha()]
    stopword = nltk.corpus.stopwords.words('english')
    content = [w for w in text_clean if w.lower() not in stopword]
    bgs = nltk.bigrams(content)
    fdist = FreqDist(bgs)
    return fdist.most_common(25)

class Vocabulary():

    def __init__(self, text):
        self.text=text

    def frequency(self, word):
        fdist = FreqDist(self.text)
        return fdist[word]

    def pos(self, word):
        self.w=word
        if len(wn.synsets(self.w))==0:
            final = None
        else: final = wn.synsets(self.w)[0].pos()
        return final

    def gloss(self, word):
        self.w=word
        if len(wn.synsets(self.w))==0:
            return None
        else:
            syns= wn.synsets(self.w)[0]
            return syns.definition()

    def kwic(self, word):
        self.w=word
        self.text.concordance(self.w)


def dot(A,B): 
    return (sum(a*b for a,b in zip(A,B)))
def cosine(a,b):
    cos=dot(a,b)/((dot(a,a)**0.5)*(dot(b,b)**0.5))
    return round(cos, 2)

def compare_to_brown(text):
    vocab = Vocabulary(text)
    vector_adventure=[]
    vector_fiction=[]
    vector_humor=[]
    vector_government=[]
    vector_news=[]
    
    vector_adventure_brown=[]
    vector_fiction_brown=[]
    vector_humor_brown=[]
    vector_government_brown=[]
    vector_news_brown=[]
    
    adventure=brown.words(categories='adventure')
    fiction=brown.words(categories='fiction')
    government=brown.words(categories='government')
    humor=brown.words(categories='humor')
    news=brown.words(categories='news')
    for (word, freq) in most_frequent_content_words(news)[:300]:
        vector_news.append(vocab.frequency(word))
        vector_news_brown.append(freq)
    for (word, freq) in most_frequent_content_words(government)[:300]:
        vector_government.append(vocab.frequency(word))
        vector_government_brown.append(freq)
    for (word, freq) in most_frequent_content_words(humor)[:300]:
        vector_humor.append(vocab.frequency(word))
        vector_humor_brown.append(freq)
    for (word, freq) in most_frequent_content_words(fiction)[:300]:
        vector_fiction.append(vocab.frequency(word))
        vector_fiction_brown.append(freq)
    for (word, freq) in most_frequent_content_words(adventure)[:300]:
        vector_adventure.append(vocab.frequency(word))
        vector_adventure_brown.append(freq)
    print("adventure",cosine(vector_adventure,vector_adventure_brown))
    print("fiction",cosine(vector_fiction,vector_fiction_brown))
    print("humor",cosine(vector_humor,vector_humor_brown))
    print("government",cosine(vector_government,vector_government_brown))
    print("news",cosine(vector_news,vector_news_brown))










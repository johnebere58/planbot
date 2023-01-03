
from nltk import *
from nltk.corpus import brown


newsWords = brown.words(categories="news")

cfd = ConditionalFreqDist(brown.tagged_words(categories='news'))

fd = FreqDist(newsWords)

brown_tagged_sents = brown.tagged_sents(categories='news')

brown_sents = brown.sents(categories='news')

print("tagged",brown_tagged_sents)
print("sentences",brown_sents)


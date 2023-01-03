
from nltk import *
from nltk.corpus import brown


	
def performance(cfd, wordlist):
    lt = dict((word, cfd[word].max()) for word in wordlist)
    baseline_tagger = UnigramTagger(model=lt, backoff=DefaultTagger('NN'))
    return baseline_tagger.evaluate(brown.tagged_sents(categories='news'))

def display():
    import pylab
    word_freqs = FreqDist(brown.words(categories='news')).most_common()
    words_by_freq = [w for (w, _) in word_freqs]
    cfd = ConditionalFreqDist(brown.tagged_words(categories='news'))
    sizes = 2 ** pylab.arange(15)
    perfs = [performance(cfd, words_by_freq[:size]) for size in sizes]
    pylab.plot(sizes, perfs, '-bo')
    pylab.title('Lookup Tagger Performance with Varying Model Size')
    pylab.xlabel('Model Size')
    pylab.ylabel('Performance')
    pylab.show()

newsWords = brown.words(categories="news")

cfd = ConditionalFreqDist(brown.tagged_words(categories='news'))

fd = FreqDist(newsWords)

brown_tagged_sents = brown.tagged_sents(categories='news')

brown_sents = brown.sents(categories='news')

utag = UnigramTagger(brown_tagged_sents).tag(brown_sents[0])

print("tagged",brown_tagged_sents)
print("sentences",brown_sents)
print("----------")
print("Utap",utag)


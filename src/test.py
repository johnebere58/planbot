from nltk import *
import re

def space():
    print("----------")

word1 = '''
Hey, i'm planning a birthday party this weekend at my place but i dunno what to do?
'''
word2 = '''
but i dunno the best route to take
'''
word3 = '''
I want to invite some friends over
'''
word4 = '''
but i very limited budget
'''
word5 = '''
and this is giving me alot of doubt
'''



sent = [word1,word2,word3,word4,word5]
tokens = [word_tokenize(word) for word in sent]

tags = [pos_tag(token) for token in tokens]

unitag = UnigramTagger(tags)

size = int(len(tags) * 0.9)

train_sents = tags[:size]
test_sents = tags[size:]

print("train",train_sents)
print("----------")
print("test sents",test_sents)
space()

utagger = UnigramTagger(train_sents)
uv = utagger.evaluate(test_sents)

print(uv)
# print(size)
# print(unitag)
# print(help.upenn_tagset('CC'))




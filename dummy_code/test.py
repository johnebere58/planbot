from nltk import *
import re

def space():
    print("----------")

word1 = '''
I willobe hosting a nuban birthday party this weekend, unless zaga
'''
word2 = '''
All the plans iona have made are not sufficient enough
'''
word3 = '''
I want to invite some friends over to have fun and eat
'''
word4 = '''
but i very limited budget and i do not want to spend much
'''
word5 = '''
Now i dont know if i should carry on the event or not
'''



sent = [word1,word2,word3,word4,word5]
tokens = [word_tokenize(word) for word in sent]

tags = [pos_tag(token) for token in tokens]

size = int(len(tags) * 0.7)

train_sents = tags[:size]
test_sents = tags[size:]

t0 = DefaultTagger('NADA')
t1 = UnigramTagger(train_sents,backoff=t0)
t2 = BigramTagger(train_sents,backoff=t1)
t3 = TrigramTagger(train_sents,backoff=t2)

# print("t0",t0)
# space(),
# print("t1",t1.context)
# space(),
# print("t2",t2)
# space(),
# print("t3",t3)
# space(),
# print(tags)
# space()
# print("train",train_sents)
# print("----------")
# print("test sents",test_sents)
# space()




# print(tags)
# space()
tag0 = t3.tag(tokens[0])
print(tag0)

uv = t3.accuracy(test_sents)
print(uv)
# print(size)
# print(unitag)
# print(help.upenn_tagset('CC'))




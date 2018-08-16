def read_data(filename):
    with open(filename, 'r') as f:
        data = [line.split('\t') for line in f.read().splitlines()]
        data = data[1:]  # header 제외

    from random import randint
    random_data = [data[randint(1, len(data))] for no in range(int(len(data) / 50))]
    return random_data


train_data = read_data('./nltk_tutorial-master/data/ratings_train.txt')
test_data = read_data('./nltk_tutorial-master/data/ratings_test.txt')
print('Train_data : {}\nsample     : {}'.format(len(train_data), train_data[:3]))
print('Test_data  : {}\nsample     : {}'.format(len(test_data), test_data[:3]))
#===
from konlpy.tag import Okt
pos_tagger = Okt()

def tokenize(doc):
    result = ['/'.join(t) for t in pos_tagger.pos(doc, norm=True, stem=True)]
    return result

train_docs = [(tokenize(row[1]), row[2])    for row in train_data]
test_docs  = [(tokenize(row[1]), row[2])    for row in test_data]

from pprint import pprint
pprint(train_docs[:2])
#===
tokens = [t   for d in train_docs
              for t in d[0]]
print("Token Total :{}\nSample : {}".format(
    len(tokens), tokens[:5]))

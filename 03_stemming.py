import time
from nltk.tokenize import TreebankWordTokenizer

text = " Don't hesitate to ask questions"

# Penn Treebank Corpus 에 따른 기준을 사용하여, 문법별로 나눈다
now = time.time()
tokenizer = TreebankWordTokenizer()
token     = tokenizer.tokenize(text)
print(time.time()-now)
print(token)

#import nltk
#nltk.download('averaged_perceptron_tagger')
from nltk import pos_tag
print(pos_tag(token))

from nltk.tokenize import WordPunctTokenizer
now = time.time()
tokenizer = WordPunctTokenizer()
token     = tokenizer.tokenize(text)
print(time.time()-now)
print(token)

#import nltk
#nltk.download('tagsets')
import nltk.help as nltk_help
nltk_help.upenn_tagset('PRP')  # 대명사
nltk_help.upenn_tagset('JJ')  # 형용사
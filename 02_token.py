#import nltk
#nltk.download('punkt')
from nltk import sent_tokenize
from nltk import word_tokenize
from nltk import FreqDist
# ! pip3 install pandas
import pandas as pd

#=== 토크나이징
text = """힘든 월요일, 아침.
힘든 직장인 분들에게. 월요일 식혜를 제공합니다"""

# sent (. 같은 토근으로) 토큰을 나누고
#print(sent_tokenize(text))

# 단어기준으로 나눔
text = word_tokenize(text)
#print(text)

#=== 빈도수 추출
# 나중에 Pandas로 바꿔줄때 dict 자료형이 필요
#print(dict(FreqDist(text)))

f         = open('./nltk_tutorial-master/data/베를린선언.txt', 'r')
texts_org = f.read()
f.close()

texts_token = word_tokenize(texts_org)
#print(FreqDist(texts_token))

texts_token_dict = dict(FreqDist(texts_token))

texts_token_series = pd.Series(texts_token_dict)
#print(texts_token_series.sort_values(ascending=False))

#=== 정규식 이용한 토크나이징
text = """Park 010-1234-1234 Kim 010-8888-9999 
Lee 010-2123-1299 한남충 010-222-9999 메갈녀 010-555-2345"""

from nltk.tokenize import RegexpTokenizer
re_capt = RegexpTokenizer(r'\d+')
print(re_capt.tokenize(text))

re_capt = RegexpTokenizer(r'[A-z]\w+')
print(re_capt.tokenize(text))

re_capt = RegexpTokenizer(r'[가-힣]\w+')
print(re_capt.tokenize(text))

re_capt = RegexpTokenizer(r'[A-z가-힣]\w+')
print(re_capt.tokenize(text))
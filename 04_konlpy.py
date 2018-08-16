import time


text = '민병삼 대령의 항명행위로 초치했다'
from konlpy.tag import Okt

now = time.time()
twitter = Okt()
print(twitter.pos(text))
print(time.time()-now)

#!/usr/bin/env python3
# -*- coding: utf8 -*-
# Version: 1.0
'''
    File name: 01_wordcloud.py
    Author: DevHyung
    Date created: 2018.08.16
    Date last modified: -
    Python Version: 3.6
    Description :
        WC
'''
# 1 : If your os MAC, Adding below code
import matplotlib
matplotlib.use('TkAgg')
# 1 : =============================
from matplotlib import rc
from wordcloud import WordCloud
import matplotlib.pyplot as plt
if __name__ == "__main__":
    f = open('./nltk_tutorial-master/data/베를린선언.txt', 'r')
    texts_org = f.read()
    f.close()
    #rc('font', family='NanumGothic')
    wcloud = WordCloud('./nltk_tutorial-master/data/D2Coding.ttf', relative_scaling=0.2).generate(texts_org)
    plt.figure(figsize=(12, 12))
    plt.imshow(wcloud, interpolation='bilinear')
    plt.axis("off")
    plt.show()
    #plt.savefig('./test.jpg')


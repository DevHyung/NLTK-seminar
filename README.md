# NLTK-seminar
## 내용
1. Token 개념
2. 형태소 / 문법 태그
3. 문장 구조 분석
4. 단어/문장의 의미분석
5. 나이브베이즈, HMM머신러닝
6. CNN, RNN, LSTM, Seq2Seq, Attention 딥러닝 이론 이해

> ### 자연어 분석과정
1. 음운론(Phonology) : 말소리를 연구 
2. 형태론(Morphology) : 단어를 정규화 / 형태소 
3. 통사론(syntax) : 문법적 구조(parsing)
4. 의미론(Semantics) : 의미차이 

> ### 토큰이란
1. 의미를 가지는 문자열 
2. 영문은 공백만으로도 토큰 나눌 수 있다
3. 한글은 합성어, 조사합성등 별도 처리를 요함

> ### Stemming (어간추출) + Tagging
1. 접사등을 제거 단어의 어간을 분리
2. 단어들이 동일한 어간으로 맵핑되게 하는것이 목적
3. Penn Treebank Corpus, WordPunctTokenizer 등의 다양한 구분기법이 NLTK 모듈에서 기본 제공
4. **하지만 한계가 존재**

> ### koNLPY 에서는 
1. 하나에서 그냥 다해줘버림
2. 문장에서 token 추출하고 -> stemming 생성후 적합한 tag를 출력
3. 이걸 Twitter 안에서 다함 개꿀띠

> ### Stop Words (불용어처리)
1. 연관성이낮은단어들을제외하고분석
2. 내용과목적에따라서,불용어처리여부및해당
목적에 맞는 불용어 말뭉치 DB등을 판단해야 한다
3. 아직 한글은 없어서 따로 만들어서 써야함
    1. 분야별(주식,리포트,연설문)정제된자료를수집한뒤 
    2. Token을 나눈 뒤 빈도대비 중요도를 측정
    3. 빈도대비중요도측정결과를저장및활용
    4. 측정은후술할tf-idf등을활용

> ### N-Gram (Token 집합)
1. 문장,절의비교분석시token갯수일치가필요 
2. 독립적/균일한관리가능한,분류기준이필요
 
> ### PMI (N-gram 상관분석)
Point wise Mutual Information점 위치 상호관계를 활용한 정보
1. 단어간의거리를비교측정하여객체의상관성을분석한다
2. 연어(근접어:collocation)관계활용하여분석가능한 객체를 생성한다 (Bi-gram, Tri-gram)
3. PMI 는 단어간의 상관관계 확률론을 근거로, 단어간의
독립을 가정할 때 발생확률 과 문서에서 측정된 동시발생확률 을 비교하여 상관성을 분석한다
 
> ### Tf-idf 상대 빈도분석
 Term Frequency-Inverse Document Frequency
1. 문서의내용을쉽게벡터로표현하는고전적방식
2. Term Frequency : 특정 용어의 발생빈도
3. (문서 Token 출현빈도) / (문서 전체 Token 갯수)
4. Inverse Document Frequency (문서 빈도의 역) 이게 6번내용 
5. 문서를이해하는데Token의중요도
6. 일반문서대비출현빈도


 

```python

```


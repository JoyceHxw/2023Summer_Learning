import jieba.analyse

filename="./regex/doupo.txt"
fp=open(filename,'r',encoding='gb18030')
content=fp.read()

# 引入停用词
jieba.analyse.set_stop_words('./regex/stopwords.txt')
# 统计词频
word_cnts=jieba.analyse.extract_tags(content,topK=50,withWeight=True)

for word_cnt in word_cnts:
    word=word_cnt[0]
    count=str(int(word_cnt[1]*1000))
    print(word,count)

fp.close()
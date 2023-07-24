# 抓取作者名，出版社名，出版日期，图书价格，图书评价，评价人数，统一书号

import requests
from bs4 import BeautifulSoup
from lxml import etree
import re

import os
import csv

import time
import random

# 生成请求头：随机获取User-Agent
user_agents = [
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; AcooBrowser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Acoo Browser; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.0.04506)",
    "Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.5; AOLBuild 4337.35; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
    "Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US)",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)",
    "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 1.0.3705; .NET CLR 1.1.4322)",
    "Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 3.0.04506.30)",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/523.15 (KHTML, like Gecko, Safari/419.3) Arora/0.3 (Change: 287 c9dfb30)",
    "Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527+ (KHTML, like Gecko, Safari/419.3) Arora/0.6",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.2pre) Gecko/20070215 K-Ninja/2.1.1",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9) Gecko/20080705 Firefox/3.0 Kapiko/3.0",
    "Mozilla/5.0 (X11; Linux i686; U;) Gecko/20070322 Kazehakase/0.4.5",
    "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.8) Gecko Fedora/1.9.0.8-1.fc10 Kazehakase/0.5.6",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/535.20 (KHTML, like Gecko) Chrome/19.0.1036.7 Safari/535.20",
    "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; fr) Presto/2.9.168 Version/11.52",
]
request_headers={
    "User-Agent":random.choice(user_agents),
    "Cookie":'',
    "Referer":"https://book.douban.com/"
}

file_name=os.getcwd()+os.sep+"doubanbook_top250_info.csv"
# 获取csv文件的写指针，指明字符集，保证可以支持汉字
fp=open(file_name,'wt',newline="",encoding="utf-8")
# 基于文件的写指针，获取csv的写指针
csv_writer=csv.writer(fp)

# 抓取每本书的详细信息
def get_book_info(url,i):
    resp=requests.get(url=url,headers=request_headers)
    status_code=resp.status_code
    if status_code==200:
        html_txt=resp.text
        # 使用xpath完成解析，借助lxml中的etree
        xpath_selector=etree.HTML(html_txt)
        book_name=xpath_selector.xpath('//*[@id="wrapper"]/h1/span/text()')[0].strip()
        try:
            # 从XML或HTML文档中选取所有id属性为"info"的后代节点中的"a"标签，并获取这些"a"标签的文本内容
            author_name=xpath_selector.xpath('//*[@id="info"]//a/text()')[0].strip()
            # 正则表达式，匹配处理作者可能含有的空白符或无作者的情况
            pattern=re.compile("\s+")
            author_name=re.sub(pattern,"",author_name) #空白符替换为空字符
        except:
            author_name="佚名"
        try:
            publisher_name=xpath_selector.xpath('//*[@id="info"]/a[1]/text()')[0].strip()
        except:
            publisher_name='无'
        publish_date=xpath_selector.xpath('//span[contains(text(),"出版年")]')[0].tail #.tail属性获取该元素的后续文本
        book_price_element=xpath_selector.xpath('//span[text()="定价:"]')
        if book_price_element!=[]:
            book_price=book_price_element[0].tail
        else:
            book_price=0.0
        book_rate=xpath_selector.xpath('//*[@id="interest_sectl"]/div/div[2]/strong/text()')[0].strip()
        person_cnt=xpath_selector.xpath('//*[@id="interest_sectl"]/div/div[2]/div/div[2]/span/a/span/text()')[0].strip()
        book_isbn=xpath_selector.xpath('//span[contains(text(),"统一书号") or contains(text(),"ISBN")]')[0].tail
        print(i,book_name,author_name,publisher_name,publish_date,book_price,book_rate,person_cnt,book_isbn)
        # 写入csv
        csv_writer.writerow((i,book_name,author_name,publisher_name,publish_date,book_price,book_rate,person_cnt,book_isbn))


# 获取每本书的连接
def get_book_links(url,i):
    j=i*25+1
    resp=requests.get(url=url,headers=request_headers)
    status_code=resp.status_code
    if status_code==200:
        html_txt=resp.text
        soup_doc=BeautifulSoup(html_txt,'html.parser')
        book_links=soup_doc.select("div.pl2 > a")
        for book_link in book_links:
            link=book_link.get("href").strip()
            get_book_info(link,j)
            j+=1
            

if __name__=="__main__":
    # 初始化csv
    csv_header_info=("排名","书名","作者名","出版社名","出版日期","图书价格","图书评价","评价人数","统一书号")
    csv_writer.writerow(csv_header_info)
    # 构建top250book列表页的url list
    # urls=[f"https://book.douban.com/top250?start={str(i)}" for i in range(0,250,25)]
    urls=[]
    i=0
    for url in urls:
        # 提取每一页中25本书的超链接地址
        get_book_links(url,i)
        time.sleep(random.randint(1,3))
        i+=1
    fp.close()

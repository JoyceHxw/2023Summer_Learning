# 获取豆瓣所有影评的相关信息，借助cssselector

import requests
from bs4 import BeautifulSoup
import lxml

# 生成uri，请求头
url_str="https://movie.douban.com/review/best/?start=0"
# url_strs=[f"https://movie.douban.com/review/best/?start={str(i) }" for i in range(0,100,10)]
# print(url_strs)
request_headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
    "Referer":"https://movie.douban.com/review/best/",
    "Accept":"*/*"
}

# 封装请求，发送，获取响应
resp=requests.get(url=url_str,headers=request_headers)
# 处理响应，获取htmltxt
status_code=resp.status_code
if status_code==200:
    html_txt=resp.text

# 使用beautifulsoup4解析html_txt为soup文档
soup_doc=BeautifulSoup(html_txt,"lxml")

# 定位
soup_doc.select
# author_name_elements=soup_doc.find(name='a',class_="name")
author_info_elements=soup_doc.select("a.name") #作者信息
movie_info_elements=soup_doc.select("a.subject-img") #电影信息

for author_element,movie_element in zip(author_info_elements,movie_info_elements):
    author_name=author_element.get_text().strip()
    author_homepage=author_element.get("href").strip()
    movie_img_element=movie_element.find(name="img")
    movie_name=movie_img_element.get("title").strip()
    movie_homepage=movie_element.get("href").strip()
    movie_cover=movie_img_element.get("src").strip()

    movie_review_info={
        "author_name":author_name,
        "author_homepage":author_homepage,
        "movie_name":movie_name,
        "movie_homepage":movie_homepage,
        "movie_cover":movie_cover
    }
    print(movie_review_info)
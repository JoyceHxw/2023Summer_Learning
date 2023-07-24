# 获取酷狗top500的歌名，歌手，时长

import requests
from bs4 import BeautifulSoup
import lxml
import time 
import random

# 生成请求头
request_headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
    "Accept":"*/*"
}

def get_music_info(url):
    resp=requests.get(url=url,headers=request_headers)
    status_code=resp.status_code
    # print(status_code)
    if status_code==200:
        html_txt=resp.text
        soup_doc=BeautifulSoup(html_txt,"lxml")
        rank_elements=soup_doc.select("span.pc_temp_num")
        music_elements=soup_doc.select("a.pc_temp_songname")
        time_elements=soup_doc.select("#rankWrap > div.pc_temp_songlist > ul > li > span.pc_temp_tips_r > span")

        for rank_element,music_element,time_element in zip(rank_elements,music_elements,time_elements):
            rank=rank_element.get_text().strip()
            try:
                song=music_element.get("title").split("-")[1].strip()
                singer=music_element.get("title").split("-")[0].strip()
                duration=time_element.get_text().strip()
            except:
                song=music_element.get("title")
                singer="none"
            data={"rank":rank,"song":song,"singer":singer,"dutation":duration}
            print(data)


if __name__=="__main__":
    # 生成urllist
    urls=[f"https://www.kugou.com/yy/rank/home/{str(i)}-8888.html" for i in range(1,24)]
    # print(urls)
    for url in urls:
        print("--------------------------------------------------")
        get_music_info(url)
        time.sleep(random.randint(1,3))
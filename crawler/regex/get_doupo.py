import requests
import re
import time

request_headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
    "Accept":"*/*"
}

fp=open('doupo.txt','a+')

def get_txt(url_str):
    resp=requests.get(url=url_str,headers=request_headers)
    status_code=resp.status_code
    if status_code==200:
        # re.findall(pattern, string, flags): 这是re模块中的函数，用于查找字符串中所有与正则表达式pattern匹配的部分，并以列表形式返回。其中：
            # pattern: 是要匹配的正则表达式模式。
            # string: 是要在其中搜索的字符串。
            # flags: 是可选的标志参数，用于修改正则表达式的行为。在这里使用了re.S标志，它表示将.匹配包括换行符在内的所有字符。
            # (.*?): 是一个非贪婪匹配，用于匹配任意字符（包括换行符），但尽可能少地匹配，直到遇到</p>结束标签。
        contents=re.findall('<p>(.*?)</p>',resp.content.decode('utf-8'), re.S) # 括号中是要获取p中的内容
        for content in contents:
            fp.write(content+'\n')


if __name__=="__main__":
    urls=[f"http://book.doupoxs.com/doupocangqiong/{str(i)}.html" for i in range(1,500)]
    for url_str in urls:
        get_txt(url_str)
        time.sleep(1)
    fp.close()
    print("end...")

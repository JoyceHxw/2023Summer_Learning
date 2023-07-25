# 借助requests-html 完成豆瓣电影页面中动态数据的获取

import time
import random
from requests_html import HTMLSession,UserAgent

# 生成url
url_str="https://movie.douban.com/"

# 生成请求头
# 借助requsts-html中的UserAgent实现
user_agent=UserAgent().random
# 借助自行生成的list获取
# user_agents = [
#     "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; AcooBrowser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
#     "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Acoo Browser; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.0.04506)",
#     "Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.5; AOLBuild 4337.35; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
#     "Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US)",
#     "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)",
#     "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 1.0.3705; .NET CLR 1.1.4322)",
#     "Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 3.0.04506.30)",
#     "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/523.15 (KHTML, like Gecko, Safari/419.3) Arora/0.3 (Change: 287 c9dfb30)",
#     "Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527+ (KHTML, like Gecko, Safari/419.3) Arora/0.6",
#     "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.2pre) Gecko/20070215 K-Ninja/2.1.1",
#     "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9) Gecko/20080705 Firefox/3.0 Kapiko/3.0",
#     "Mozilla/5.0 (X11; Linux i686; U;) Gecko/20070322 Kazehakase/0.4.5",
#     "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.8) Gecko Fedora/1.9.0.8-1.fc10 Kazehakase/0.5.6",
#     "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
#     "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/535.20 (KHTML, like Gecko) Chrome/19.0.1036.7 Safari/535.20",
#     "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; fr) Presto/2.9.168 Version/11.52",
# ]

# user_agent=random.choice(user_agents)
request_headers={"User-Agent": user_agent}

# 发送请求，获取响应
# 创建Http|Html会话连接
session=HTMLSession()
# 提供额外参数，设置连接和读取超时，不校验https
resp=session.get(url=url_str,headers=request_headers,timeout=(2,5),verify=False)
time.sleep(2)

status_code=resp.status_code
if status_code==200:
    # 执行动态渲染，第一次执行会下载pyppeteer浏览器资源
    resp.html.render(sleep=2,retries=3, timeout=20000)
    html_txt=resp.html.html  # 动态渲染可能导致数据重复，需要去重
    print(resp.html.html)
    with open("./douban_movie.txt",mode='w',encoding='utf-8') as file:
        file.write(html_txt)
    # print(html_txt)
    # # 基于html_text完成解析、定位、提取
    # resp.html.find==cssselector
    # resp.html.xpath==xpath
    
session.close()
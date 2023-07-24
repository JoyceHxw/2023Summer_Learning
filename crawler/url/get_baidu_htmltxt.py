import urllib.request

# 0.准备要访问的url https://www.baidu.com
url_str="https://www.baidu.com"
# 1.封装请求（提供要访问的URL，访问的方法），同时给出请求头User-Agent（模仿浏览器的请求）
request_headers={'User-Agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
                 "Referer":"http://www.douban.com",
                 "Connection":"keep-alive"
                 }
# 生成请求实例对象，同时提供URL，请求标头，
request=urllib.request.Request(url=url_str,method="GET",headers=request_headers)
# 2.发送请求，获取响应
response=urllib.request.urlopen(url=request,timeout=5)
# 3.响应处理
# 获取状态码
status_code=response.status
# 获取响应返回的htmltext
html_txt=response.read().decode("utf-8")
print(html_txt)
# 获取响应头信息
response_headers=response.getheaders()
content_type=response.getheader("Content-Type")
print("Response Headers: ", response_headers)
print("Content Type: ",content_type)
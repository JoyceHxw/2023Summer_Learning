# requests模块的功能：发送请求，获取响应
import requests

# 生成uri，请求头
url_str="https://movie.douban.com/review/best/"
request_headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
    "Referer":"https://movie.douban.com/review/best/",
    "Accept":"*/*"
}

# 发送请求，获得响应
response=requests.get(url=url_str,headers=request_headers)
status_code=response.status_code
response_url=response.url
response_headers=response.headers
response_encode=response.encoding
print(status_code)
print(response_url)
print(response_headers)
print(response_encode)

# 获取响应数据
html_txt=response.text
print(html_txt)
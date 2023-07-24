import os
# 获取指定资源（urllib多作为网络资源下载的使用）
import urllib.request
# 提供uri	https://www.baidu.com/img/PCtm_d9c8750bed0b3c7d089fa7d55720d6cf.png
# 0.生成图片资源的uri
# uri_src="https://www.baidu.com/img/PCtm_d9c8750bed0b3c7d089fa7d55720d6cf.png"
uri_src="https://imdb-video.media-imdb.com/vi3657024025/1434659607842-pgv4ql-1653498218293.mp4?Expires=1690111454&Signature=CvtlP8ulu0Ezf4uz-OCfKbMMt4I1u09wBbOc~Er3pCjA0VkbhRspYNeu9877o-GjripWD-p1XhiEMwQo3AiYxpn1LfcVywgB~5jCC-jOMhyaLwdLFbqoy~~cSD6mGBbCYhWngTB3H~0INSZcUsHXcCdO4hzRcdkeAhWU5t9ibYUA45ChopP7VyypTcI2Oqnlf5R9KK1lT0JvjTLL2FVNVwTUdhD0O1FuD9ca1HmVpmWiPynKFVHKqY2MfLWoCtHRDQiK9InowOTVwqBdaR37VE6KZx~utvgfNzLi26ZgqVt0GbteJagkpn-U9iGfebUGntCSTn3H8k5JDa4F-TmWZg__&Key-Pair-Id=APKAIFLZBVQZ24NQH3KA"
# 1.封装请求
request_headers={'User-Agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"}
request=urllib.request.Request(url=uri_src,headers=request_headers,method="GET")
# 2.发送请求，获取响应
response=urllib.request.urlopen(url=request)
# 3.处理响应
status_code=response.status
if status_code==200:
    response_data=response.read()  #图片资源的数据
    # file_name="baidu_logo.png"
    file_name="mission.mp4"
    file_path=os.getcwd()
    if not os.path.exists(file_path):
        os.mkdir(file_path)
    with open(file=file_path+os.sep+file_name,mode='wb') as fp:
        fp.write(response_data)


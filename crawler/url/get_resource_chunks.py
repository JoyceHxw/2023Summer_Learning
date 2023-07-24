import os
import urllib.request

# 资源的uri
uri_src = "https://imdb-video.media-imdb.com/vi1670760217/1434659607842-pgv4ql-1689772608918.mp4?Expires=1690208320&Signature=bi6Gf0lHlrW-CD3a0Nf2rEtnqfA1rdPPHwDTisu~MRahR8L1o6uVcS5oMjWeZnF6Az8xRVspbQlz2okV~HPDWtjiBez3~uqE8lVq4ItOYwxqnzN3KZgR061iXMgIliJQrev6SbG7NtkuFwLWP8-OdpCFBfStDNc1RHpzPg8eDFB9Tfz7~lDOLicPqYR5klHTIylviTP2mthhfLBH-vBO0C8dXXVcNETA~RWpSSHhl1uiUuX9QUHY4rrhSP5~VmBfEufR90iYJGogv6nnE58-3Qmo-oGI9-8ld37vnOQjgl7tidAWovBWnwGu9NW2zAuJlSimZQn0VFJR-CnXzR32cA__&Key-Pair-Id=APKAIFLZBVQZ24NQH3KA"

# 封装请求
request_headers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"}
request = urllib.request.Request(url=uri_src, headers=request_headers, method="GET")

response = urllib.request.urlopen(url=request)

status_code = response.status
if status_code == 200:
    file_name = "imdb_trailer.mp4"
    file_path = os.getcwd()
    if not os.path.exists(file_path):
        os.mkdir(file_path)

    # 抓取文件大小（字节）
    file_size = int(response.headers["Content-Length"]) if "Content-Length" in response.headers else None
    print(file_size)

    with open(file=file_path + os.sep + file_name, mode='wb') as fp:
        # 每一块的字节大小
        chunk_size = 8192  # 8MB
        downloaded_size = 0

        while True:
            # 按规定的每块字节大小读取
            chunk = response.read(chunk_size)
            if not chunk:
                break

            downloaded_size += len(chunk)
            fp.write(chunk)

            # 进度展示
            if file_size:
                progress = downloaded_size / file_size * 100
                print(f"下载中... {progress:.2f}%")

    print("下载完成！")
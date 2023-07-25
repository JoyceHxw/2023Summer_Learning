from bs4 import BeautifulSoup
import csv

with open("./douban_movie.txt","r",encoding='utf-8') as file:
    saved_html_txt = file.read()
# print(saved_html_txt)

# max_characters_per_batch = 1000  # 设置每批输出的最大字符数
# start_index = 0
# while start_index < len(saved_html_txt):
#     end_index = start_index + max_characters_per_batch
#     print(saved_html_txt[start_index:end_index])
#     start_index = end_index

fp=open('./douban_movie.csv',"wt",newline="",encoding="utf-8")
csv_writer=csv.writer(fp)
csv_header_info=("连接","名称","评价")
csv_writer.writerow(csv_header_info)

soup_doc=BeautifulSoup(saved_html_txt,'html.parser')
# movie_link_elements=soup_doc.select('#content > div > div.article > div.gaia.gaia-lite.gaia-movie.slide-mode > div.list-wp > div > div.slide-container > div > div > a')
# movie_name_elements=soup_doc.select('#content > div > div.article > div.gaia.gaia-lite.gaia-movie.slide-mode > div.list-wp > div > div.slide-container > div > div > a > div > img')
# movie_rate_elements=soup_doc.select('#content > div > div.article > div.gaia.gaia-lite.gaia-movie.slide-mode > div.list-wp > div > div.slide-container > div > div > a > p > strong')
movie_link_elements=soup_doc.select('a.item')
movie_name_elements=soup_doc.select('div.cover-wp img')
movie_rate_elements=soup_doc.select('strong')


for movie_link_element, movie_name_element,movie_rate_element in zip(movie_link_elements,movie_name_elements,movie_rate_elements):
    movie_link=movie_link_element.get("href").strip()
    movie_name=movie_name_element.get("alt").strip()
    movie_rate=movie_rate_element.get_text().strip()
    csv_writer.writerow((movie_link,movie_name,movie_rate))
    print(movie_link,movie_name,movie_rate)

fp.close()
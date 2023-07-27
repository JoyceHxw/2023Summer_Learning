# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import csv
from sqlalchemy import create_engine,text
from sqlalchemy.exc import SQLAlchemyError

class KnowledgePipeline:
    def __init__(self) -> None:
        # csv_fp=open("agriculture_knowledge.csv",'w',encoding="gb18030",newline="")
        # csv_writer=csv.writer(csv_fp)
        # csv_header=('title','link','create_time','image','content')
        # csv_writer.writerow(csv_header)
        # self.csv_writer=csv_writer

        self.engine = create_engine('mysql+pymysql://root:2214563@localhost:3306/mysql?charset=utf8')

    def process_item(self, item, spider):
        # self.csv_writer.writerow((item['title'],item['link'],item['create_time'],item['image'],item['content']))
        try:
            table_name = 'agriculture_knowledge'
            title=item['title'][0]
            link=item['link']
            create_time=item['create_time'][0]
            if len(item['image'])>0:
                image=item['image'][0]
            else:
                image=""
            content=item['content'][0]
            insert_statement = text('INSERT INTO agriculture_knowledge(title, link, create_time, image, content) VALUES (:title, :link, :create_time, :image, :content)')
            with self.engine.connect() as conn:
                # data = (title, link,create_time, image, content)
                data = {
                    'title': title,
                    'link': link,
                    'create_time': create_time,
                    'image': image,
                    'content': content
                }
                print(data)
                conn.execute(insert_statement,[data])
                conn.commit()
        except SQLAlchemyError as e:
            print("Error inserting data into the database:", e)
        return item

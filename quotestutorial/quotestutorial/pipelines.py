# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import sqlite3



class QuotestutorialPipeline:


    def __init__(self):
        self.creat_connection()
        self.creat_table()

    def creat_connection(self):
        self.conn = sqlite3.connect('myquotes.db')
        self.curr = self.conn.cursor()

    
    def creat_table(self):
        self.curr.execute("""DROP TABLE IF EXISTS quotes_tb""")

        self.curr.execute("""CREATE TABLE quotes_tb(
            quote TEXT,
            author TEXT,
            tag TEXT)
        """)

    def process_item(self, item, spider):
        self.store_db(item)
        return item


    def store_db(self, item):
        self.curr.execute("""INSERT INTO quotes_tb VALUES (?, ?, ?)""",(
            item['quote'][0],
            item['author'][0],
            item['tag'][0]
            )
        )
        self.conn.commit()
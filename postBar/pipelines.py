# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from openpyxl import Workbook


class PostbarPipeline(object):
    wb = Workbook()
    ws = wb.active
    ws.append(['title', 'author', 'url', 'connect', 'nums'])
    def process_item(self, item, spider):
        line = [item['title'], item['author'], item['url'], item['connect'], item['nums'][0]]  # 把数据每一行整理出来
        self.ws.append(line)  # 将数据一行的形式添加到xlsx中
        self.wb.save('network.xlsx')  # 保存x
        lsx文件
        return item

# 链接mysql
# import pymysql
#
# class PostbarPipeline(object):
#     def process_item(self, item, spider):
#         cur = self.conn.cursor()
#         sql = "INSERT INTO network VALUES (Null,'%s','%s','%s','%s','%s')" % (
#             item["title"], item["url"], item["author"], item["connect"], item["nums"])
#         cur.execute(sql)
#         cur.close()
#
#
#
#         return item
#
#     def open_spider(self, spider):
#         try:
#             self.conn = pymysql.connect(
#                 host="localhost",
#                 port=3306,
#                 user="root",
#                 passwd="accp",
#                 db="spider",
#                 charset="utf8"
#             )
#             self.conn.autocommit(True)
#         except Exception as e:
#             print("链接数据库失败:" + e)
#
#     def close_spider(self, spider):
#         if self.conn:
#             self.conn.close()
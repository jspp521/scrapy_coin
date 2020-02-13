# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# class FiltPipeline(object):
#     def process_item(self, item, spider):
#         return item

import pymysql

class FiltPipeline(object):
    def __init__(self):
        self.connect = pymysql.connect(host='x', user='x', passwd='x', db='x') 
        self.cursor = self.connect.cursor()
        print("连接数据库成功")

    def process_item(self, item, spider):
        for i in range(0,len(item['value'])):
            insert_sql = "insert into scrapy_test_1 VALUES (\"{}\",\"{}\",\"{}\",\"{}\");".format(str(item['from1'][i]), str(item['to'][i]), str(item['time'][i]), str(item['value'][i]).replace(',',''))
            print(insert_sql)
            self.cursor.execute(insert_sql)
        self.connect.commit()
        
    def close_spider(self, spider):
        self.cursor.close()
        self.connect.close()
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pandas as pd
# openpyxl 导入
from openpyxl import Workbook
class IrodoriPipeline:
    def open_spider(self, spider):
        print('爬虫开始运行')
        # self.wb = Workbook()
        # self.sheet = self.wb.create_sheet("Mysheet")
        pass

    def process_item(self, item, spider):
        print('要处理的数据',item)
        # self.sheet.append([item['name'], item['avatar'], item['url']])
        return item
    def close_spider(self, spider):
        # self.wb.save('new_example.xlsx')
        # print('爬虫结束运行')
        pass



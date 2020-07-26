# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class StackPipeline(object):
    def process_item(self, item, spider):
        return item


import pymongo
from scrapy.conf import settings
from scrapy.exceptions import DropItem
# from scrapy import log


class MongoDBPipeline(object):

    def __init__(self):
        connection = pymongo.MongoClient(
            settings['MONGODB_SERVER']
        )
        # db = client.test
        self.db = connection[settings['MONGODB_DB']]
        self.collection = self.db[settings['MONGODB_COLLECTION']]

    def process_item(self, item, spider):
        valid = True
        for data in item:
            # print(self.db[settings['MONGODB_COLLECTION']].find({'code': item['code']}).count())
            if self.db[settings['MONGODB_COLLECTION']].find({'code': item['code']}).count() > 0:
                valid = False
        if valid:
            self.collection.insert(dict(item))
        return item
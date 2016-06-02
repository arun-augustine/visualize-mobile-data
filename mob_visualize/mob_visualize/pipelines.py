# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import MySQLdb

class MobVisualizePipeline(object):
      def process_item(self, item, spider):
        return item
  # def __init__(self):
  #   self.conn = MySQLdb.connect(user='root', passwd='sayone', db='gitpush', host='localhost', charset="utf8", use_unicode=True)
  #   self.cursor = self.conn.cursor()
  #
  # def process_item(self, item, spider):
  #   try:
  #     self.cursor.execute("""INSERT INTO mobile_data (name,launch_date,lowest_price,battery,camera,processor,ram,os,display,review_count,user_rating)
  #                         VALUES (%s, %s, %s,%s, %s, %s,%s, %s, %s,%s, %s)""",
  #                         (item['name'].encode('utf-8'),item['launch_date'], item['lowest_price'], item['features']['Battery'].encode('utf-8'),
  #                         item['features']['Camera'].encode('utf-8'), item['features']['Processor'].encode('utf-8'), item['features']['RAM'].encode('utf-8'),
  #                         item['features']['Operating System'].encode('utf-8'), item['features']['Display'].encode('utf-8'), item['review_count'],
  #                         item['user_rating']))
  #     self.conn.commit()
  #
  #   except MySQLdb.Error, e:
  #     print "Error %d: %s" % (e.args[0], e.args[1])
  #
  #   return item
  #

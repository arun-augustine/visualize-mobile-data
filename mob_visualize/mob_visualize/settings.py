# -*- coding: utf-8 -*-

# Scrapy settings for mob_visualize project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#
import plotly.tools as tls

tls.set_credentials_file(username='shamily', api_key='bifvgaoelb')

BOT_NAME = 'mob_visualize'

SPIDER_MODULES = ['mob_visualize.spiders']
NEWSPIDER_MODULE = 'mob_visualize.spiders'


ITEM_PIPELINES = {
    'mob_visualize.pipelines.MobVisualizePipeline': 500,
}

DB_SERVER = 'MySQLdb'            # For detail, please see twisted doc
DB_CONNECT = {
    'db': 'gitpush',             # Your db
    'user': 'root',              #
    'passwd': 'sayone',            #
    'host': 'localhost',      # Your Server
    'charset': 'utf8',
    'use_unicode': True,
}




# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'mob_visualize (+http://www.yourdomain.com)'

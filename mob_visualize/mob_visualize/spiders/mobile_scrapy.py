import scrapy
import plotly

from ..import items
from lxml import html
from scrapy.http import Request

import plotly.plotly as py
import plotly.graph_objs as go

from scrapy import signals
from scrapy.xlib.pydispatch import dispatcher


class MobileData(scrapy.Spider):
    items = []
    name = "mobiledata"
    domain = 'http://www.themobileindian.com/'
    start_urls = ['http://www.themobileindian.com/top-10-latest-mobiles']

    def __init__(self):
        dispatcher.connect(self.spider_closed, signals.spider_closed)

    def spider_closed(self, spider):
        """
        Ploting the mobile details based on rating after the spider signal is closed.
        :param spider:
        :return:
        """
        name_list = []
        rating = []
        feature_list = []
        for item in self.items:
            name_list.append(item['name'])
            rating.append(item['user_rating'])
            feature_list.append((item['features']['Battery'],item['features']['Camera'],item['features']['Display'],item['features']['Processor'],item['features']['RAM']))

        trace0 = go.Bar(
            x=name_list,
            y=rating,
            text=feature_list,
            marker=dict(
                color='rgb(158,202,225)',
                line=dict(
                    color='rgb(8,48,107)',
                    width=1.5,
                    )
                 ),
            opacity=0.6
                )
        data = [trace0]
        layout = go.Layout(
            title='Mobile review',
        )
        fig = go.Figure(data=data, layout=layout)
        plot_url = py.plot(fig, filename='mobile_review')

    def parse(self, response):
        """
        Parse the list of latest 10 mobiles
        :param response:
        :return:
        """
        doc = html.fromstring(response.body)
        sets = doc.xpath('.//div[@class="handInfo"]//a')
        for each_set in sets:
            url = self._apply_schema_to_url(each_set.attrib['href'])
            yield Request(url, callback=self.parse_details)

    def parse_details(self, response):
        """
        Parse the details of each mobile
        :param response:
        :return:
        """
        doc = html.fromstring(response.body)
        feature = {}
        whole_data = doc.xpath('.//div[@class="model-spec"]')[0]
        name = whole_data.xpath('.//div[@class="model-info-wrp"]/h1[@itemprop="name"]/text()')
        release_date = whole_data.xpath('.//span[@itemprop="releaseDate"]/text()')
        other_details = whole_data.xpath('.//div[@class="model-info-with-price"]//dl/dd/text()')[1:]
        for data in other_details:
            split_data = data.split(':')
            feature.update({split_data[0].strip(): split_data[1].strip()})
        user_rating = doc.xpath('.//div[@itemprop="ratingValue"]/text()')
        review_count = doc.xpath('.//span[@itemprop="reviewCount"]/text()')
        price_details = doc.xpath('.//a[@id="priceavailable"]/p/text()')[0]
        item = items.MobVisualizeItem()
        item['name'] = name[0]
        if release_date:
            item['launch_date'] = release_date[0]
        else:
            item['launch_date'] = 'not specified'
        item['user_rating'] = user_rating[0].strip()
        item['features'] = feature
        item['review_count'] = review_count[0].strip()
        item['lowest_price'] = price_details
        self.items.append(item)
        yield item

    def _apply_schema_to_url(self, url):
        """
        Url formatting
        :param url:
        :return:
        """
        if self.domain in url:
            return url
        url = self.domain + url
        return url

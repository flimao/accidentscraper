# decompyle3 version 3.3.2
# Python bytecode 3.8 (3413)
# Decompiled from: Python 3.8.5 (default, Aug  5 2020, 09:44:06) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: C:\Users\bdzp\Pessoal\software\python\projetos\asn-scraper\asnscraper\disasters.py
# Compiled at: 2020-08-25 22:14:27
# Size of source mod 2**32: 1919 bytes
from datetime import datetime as dt
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from asnscraper.items import DisasterRaw, AirportRaw
import re
RE_LISTING = '.*/dblist\\.php\\?(Year)=(1920|2017)$'
RE_RECORD = '.*/record\\.php\\?id=((\\d{8})-(\\d+))$'
RE_AIRPORT = '.*/airport\\.php\\?id=(\\w+)$'

class DisasterSpider(CrawlSpider):
    name = 'disasters'
    allowed_domains = ['aviation-safety.net']
    start_urls = ['https://aviation-safety.net/database/']
    rules = [
     Rule(LinkExtractor(allow=RE_LISTING), callback='parse_list', follow=True),
     Rule(LinkExtractor(allow=RE_RECORD), callback='parse_record', follow=True),
     Rule(LinkExtractor(allow=RE_AIRPORT), callback='parse_airport', follow=False)]

    def parse_list(self, response):
        m = re.match(RE_LISTING, response.url)
        print(f"This is a database listing WHERE '{m[1]}' = '{m[2]}'")

    def parse_airport(self, response):
        id = re.match(RE_AIRPORT, response.url)
        airportraw = AirportRaw()
        airportfields = response.xpath("//a[@name='general']/div[@class='infobox']//table[1]//tr")
        airportname = response.xpath("//a[@name='general']/div[@class='infobox']/span/text()")
        airportraw['id'] = id[1]
        airportraw['name'] = airportname
        airportraw['allfields'] = airportfields
        return airportraw

    def parse_record(self, response):
        id = re.match(RE_RECORD, response.url)
        disasterraw = DisasterRaw()
        disasterfields = response.xpath("//div[@class='innertube']//table[1]//tr")
        disasterraw['id'] = id[1]
        disasterraw['date'] = dt.strptime(id[2], '%Y%m%d')
        disasterraw['allfields'] = disasterfields
        return disasterraw
# okay decompiling __pycache__\disasters.cpython-38.pyc

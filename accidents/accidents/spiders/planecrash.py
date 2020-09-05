# -*- coding: utf-8 -*-

from datetime import datetime as dt
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from accidents.items import PlaneCrashDisasterRaw
import re


RE_LISTING = r'.*/(1920)/\1\.html?.*'
RE_RECORD = r'.*/(\d{4})/(\1-\d{1,10})\.html?.*'


class PlaneCrashSpider(CrawlSpider):
    name = 'planecrash'
    allowed_domains = ['planecrashinfo.com']
    start_urls = ['http://www.planecrashinfo.com/database.htm']
    rules = [
        Rule(LinkExtractor(allow=RE_LISTING), callback='parse_list', follow=True),
        Rule(LinkExtractor(allow=RE_RECORD), callback='parse_record', follow=False)
    ]

    @staticmethod
    def parse_list(response):
        m = re.match(RE_LISTING, response.url)
        print(f"Database listing WHERE 'year' = '{m[1]}' (url = '{response.url}')")

    @staticmethod
    def parse_record(response):
        id = re.match(RE_RECORD, response.url)
        disasterraw = PlaneCrashDisasterRaw()
        disasterfields = response.xpath("//table//tr")[1:]
        print(id.groups())
        disasterraw['id'] = id[2]
        disasterraw['date'] = dt.strptime(id[1], '%Y')
        disasterraw['allfields'] = disasterfields
        print(f"Accident listing WHERE 'id' = '{disasterraw['id']}'")
        return disasterraw

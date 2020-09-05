# -*- coding: utf-8 -*-

from datetime import datetime as dt
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from accidents.items import PlaneCrashDisasterRaw
import re


RE_LISTING_PAT = r'.*/(1920)/\1\.html?.*'
RE_RECORD_PAT = r'.*/(\d{4})/(\1-\d{1,10})\.html?.*'
#RE_RECORD_PAT = r'.*/(\d{4})/(\1-1)\.html?.*'  # testing only

RE_LISTING = re.compile(RE_LISTING_PAT)
RE_RECORD = re.compile(RE_RECORD_PAT)


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
        m = RE_LISTING.match(response.url)
        print(f"Database listing WHERE 'year' = '{m[1]}' (url = '{response.url}')")

    @staticmethod
    def parse_record(response):
        id = RE_RECORD.match(response.url)
        disasterraw = PlaneCrashDisasterRaw()

        disasterfields = response.xpath("//table//tr")[1:]
        disasterraw['id'] = id[2]
        disasterraw['date'] = dt.strptime(id[1], '%Y')
        disasterraw['allfields'] = disasterfields
        print(f"Accident listing WHERE 'id' = '{disasterraw['id']}' (url = '{response.url}')")
        return disasterraw

# -*- coding: utf-8 -*-

from datetime import datetime as dt
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from accidents.items import ASNDisasterRaw, AirportRaw
import re


RE_LISTING = r'.*/dblist\.php\?(Year)=(1920)$'
RE_RECORD = r'.*/record\.php\?id=((\d{8})-(\d+))$'
RE_AIRPORT = r'.*/airport\.php\?id=(\w+)$'


class ASNSpider(CrawlSpider):
    name = 'asn'
    allowed_domains = ['aviation-safety.net']
    start_urls = ['https://aviation-safety.net/database/']
    rules = [
        Rule(LinkExtractor(allow=RE_LISTING), callback='parse_list', follow=True),
        Rule(LinkExtractor(allow=RE_RECORD), callback='parse_record', follow=True),
        Rule(LinkExtractor(allow=RE_AIRPORT), callback='parse_airport', follow=False)
    ]

    @staticmethod
    def parse_list(response):
        m = re.match(RE_LISTING, response.url)
        print(f"Database listing WHERE '{m[1]}' = '{m[2]}'")

    @staticmethod
    def parse_airport(response):
        id = re.match(RE_AIRPORT, response.url)
        airportraw = AirportRaw()
        airportfields = response.xpath("//a[@name='general']/div[@class='infobox']//table[1]//tr")
        airportname = response.xpath("//a[@name='general']/div[@class='infobox']/span/text()")
        airportraw['id'] = id[1]
        airportraw['name'] = airportname
        airportraw['allfields'] = airportfields
        print(f"Airport listing WHERE 'id' = '{airportraw['id']}'")
        return airportraw

    @staticmethod
    def parse_record(response):
        id = re.match(RE_RECORD, response.url)
        disasterraw = ASNDisasterRaw()
        disasterfields = response.xpath("//div[@class='innertube']//table[1]//tr")
        disasterraw['id'] = id[1]
        disasterraw['date'] = dt.strptime(id[2], '%Y%m%d')
        disasterraw['allfields'] = disasterfields
        print(f"Accident listing WHERE 'id' = '{disasterraw['id']}'")
        return disasterraw

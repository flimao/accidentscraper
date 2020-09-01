# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

# decompyle3 version 3.3.2
# Python bytecode 3.8 (3413)
# Decompiled from: Python 3.8.5 (default, Aug  5 2020, 09:44:06) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: C:\Users\bdzp\Pessoal\software\python\projetos\asn-scraper\asnscraper\asnscraper\items.py
# Compiled at: 2020-08-25 22:16:21
# Size of source mod 2**32: 1467 bytes

import scrapy


class DisasterRaw(scrapy.Item):
    id = scrapy.Field()
    allfields = scrapy.Field()
    date = scrapy.Field()
    ap_from = scrapy.Field()
    ap_to = scrapy.Field()


class Disaster(scrapy.Item):
    id = scrapy.Field()
    datetime = scrapy.Field()
    type = scrapy.Field()
    operator = scrapy.Field()
    aircraft = scrapy.Field()
    crew_deaths = scrapy.Field()
    crew_total = scrapy.Field()
    passenger_deaths = scrapy.Field()
    passenger_total = scrapy.Field()
    ground_deaths = scrapy.Field()
    souls_deaths = scrapy.Field()
    souls_total = scrapy.Field()
    damage = scrapy.Field()
    fate = scrapy.Field()
    location = scrapy.Field()
    flightphase = scrapy.Field()
    nature = scrapy.Field()
    ap_from = scrapy.Field()
    ap_to = scrapy.Field()
    flightnumber = scrapy.Field()
    narrative = scrapy.Field()


class AirportRaw(scrapy.Item):
    id = scrapy.Field()
    name = scrapy.Field()
    allfields = scrapy.Field()


class Airport(scrapy.Item):
    id = scrapy.Field()
    name = scrapy.Field()
    country = scrapy.Field()
    iata = scrapy.Field()
    icao = scrapy.Field()
    elevation = scrapy.Field()
    elevation_unit = scrapy.Field()
    dateopened = scrapy.Field()
# okay decompiling __pycache__\items.cpython-38.pyc

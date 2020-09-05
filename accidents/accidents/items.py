# -*- coding: utf-8 -*-

import scrapy


class DisasterRaw(scrapy.Item):
    id = scrapy.Field()
    allfields = scrapy.Field()
    date = scrapy.Field()
    ap_from = scrapy.Field()
    ap_to = scrapy.Field()


class Disaster(scrapy.Item):
    id = scrapy.Field()
    source = scrapy.Field()
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
    summary = scrapy.Field()
    route = scrapy.Field()


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

# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

# decompyle3 version 3.3.2
# Python bytecode 3.8 (3413)
# Decompiled from: Python 3.8.5 (default, Aug  5 2020, 09:44:06) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: C:\Users\bdzp\Pessoal\software\python\projetos\asn-scraper\asnscraper\asnscraper\pipelines.py
# Compiled at: 2020-08-25 23:10:47
# Size of source mod 2**32: 4778 bytes

import os.path
from datetime import timedelta as td
from scrapy.exporters import CsvItemExporter
from scrapy.exceptions import DropItem
from asnscraper.items import Disaster, DisasterRaw, Airport, AirportRaw
import re

DATADIR = r'..\data'


class ExportPipeline:
    dbs = [Airport, Disaster]
    exporters = {}

    @staticmethod
    def dbname(db):
        return db.__name__.lower()

    @staticmethod
    def file_path(file, folder = DATADIR):
        return os.path.abspath(os.path.join(folder, file))

    def open_spider(self, spider):
        for db in self.dbs:
            db_name = self.dbname(db)
            f = open(self.file_path(f"{db_name}s.csv"), 'wb')
            e = CsvItemExporter(f)
            e.start_exporting()
            self.exporters[db_name] = e

        return spider

    def close_spider(self, spider):
        for e in self.exporters.values():
            e.finish_exporting()

        return spider

    def process_item(self, item, spider):
        for db in self.dbs:
            if isinstance(item, db):
                db_name = self.dbname(db)
                self.exporters[db_name].export_item(item)
                print(f'ExportPipeline in {db_name}: {item}')
        else:
            raise DropItem


class AirportPipeline:

    def process_item(self, raw, spider):
        if not isinstance(raw, AirportRaw):
            return raw
        # df = raw['allfields']
        airport = Airport()
        airport['id'] = raw['id']
        airport['name'] = raw['name'].extract()[0].strip()
        return airport


class DisasterPipeline:

    def process_item(self, raw, spider):
        if not isinstance(raw, DisasterRaw):
            return raw
        df = raw['allfields']
        disaster = Disaster()
        disaster['id'] = raw['id']
        timestr = extract_field(field='Time', df=df)
        try:
            hours, minutes = re.match(r'(\d\d):(\d\d)', timestr).groups()
        except (AttributeError, TypeError):
            hours, minutes = (0, 0)
        finally:
            deltat = td(hours=(int(hours)), minutes=(int(minutes)))
            total_dt = raw['date'] + deltat
            disaster['datetime'] = total_dt
            disaster['crew_deaths'], disaster['crew_total'] = fatalities('Crew', df=df)
            disaster['passenger_deaths'], disaster['passenger_total'] = \
                fatalities('Passengers', df=df)
            disaster['souls_deaths'], disaster['souls_total'] = fatalities('Total', df=df)
            disaster['ground_deaths'] = fatalities_ground(df=df)
            disaster['damage'] = extract_field(field='Aircraft damage', df=df)
            disaster['fate'] = extract_field(field='Aircraft fate', df=df)
            disaster['aircraft'] = extract_field(field='Registration', df=df)
            disaster['location'] = extract_field(field='Location', df=df)
            disaster['flightphase'] = extract_field(field='Phase', df=df)
            disaster['nature'] = extract_field(field='Nature', df=df)
            disaster['ap_from'] = extract_field(field='Departure airport', df=df)
            disaster['ap_to'] = extract_field(field='Destination airport', df=df)
            disaster['flightnumber'] = extract_field(field='Flightnumber', df=df)
            return disaster


def extract_field(field, df):
    query = f'td[@class="caption" and text()="{field}:"]/following-sibling::td//text()'
    query2 = f'td[@class="caption"]//*[text()="{field}:"]/' \
             f'ancestor::td/following-sibling::td//text()'
    ret = df.xpath(query).extract() or df.xpath(query2).extract()
    if isinstance(ret, list):
        if len(ret) == 0:
            return
        ret = [str(r) for r in ret]
        return ''.join(ret).strip()
    if isinstance(ret, str):
        return ret.strip()
    return ret


def fatalities(field, df):
    fstr = extract_field(field=field, df=df)
    if fstr is None:
        return
    fatal = re.match(r'.*[Ff]atalities:\s*(\d*)\s*/\s*[Oo]ccupants:\s*(\d*).*', fstr)
    f_deaths = int(fatal[1]) if fatal[1] != '' else None
    f_total = int(fatal[2]) if fatal[2] != '' else None
    return (
     f_deaths, f_total)


def fatalities_ground(df):
    fstr = extract_field(field='Ground casualties', df=df)
    if fstr is None:
        return
    fatal = re.match(r'.*[Ff]atalities:\s*(\d*)\s*.*', fstr)
    if fatal is None:
        return
    f_deaths = int(fatal[1]) if fatal[1] != '' else None
    return f_deaths
# okay decompiling __pycache__\pipelines.cpython-38.pyc

# decompyle3 version 3.3.2
# Python bytecode 3.8 (3413)
# Decompiled from: Python 3.8.5 (default, Aug  5 2020, 09:44:06) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: C:\Users\bdzp\Pessoal\software\python\projetos\asn-scraper\asnscraper\asnscraper\settings.py
# Compiled at: 2020-08-25 22:39:49
# Size of source mod 2**32: 3206 bytes
BOT_NAME = 'asnscraper'
SPIDER_MODULES = [
 'asnscraper.spiders']
NEWSPIDER_MODULE = 'asnscraper.spiders'
ROBOTSTXT_OBEY = True
TELNETCONSOLE_ENABLED = False
ITEM_PIPELINES = {'asnscraper.pipelines.AirportPipeline':200, 
 'asnscraper.pipelines.DisasterPipeline':300, 
 'asnscraper.pipelines.ExportPipeline':1000}
AUTOTHROTTLE_ENABLED = True
AUTOTHROTTLE_START_DELAY = 3
AUTOTHROTTLE_MAX_DELAY = 30
AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
AUTOTHROTTLE_DEBUG = True
HTTPCACHE_ENABLED = True
HTTPCACHE_EXPIRATION_SECS = 2592000
HTTPCACHE_DIR = 'httpcache'
HTTPCACHE_IGNORE_HTTP_CODES = []
HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
# okay decompiling __pycache__\settings.cpython-38.pyc

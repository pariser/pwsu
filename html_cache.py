#!/usr/bin/python
import os
import urllib2
import logging
import codecs

_opener = urllib2.build_opener()
_opener.addheaders = [('User-agent', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:8.0) Gecko/20100101 Firefox/8.0')]

class HTMLCache(object):

    # Configuration

    _cache_dir = "~/data/html_cache"
    _slash_char = '~'
    _logger = logging.getLogger(__name__)

    @classmethod
    def set_opts(cls, opts={}):
        if 'logger' in  opts:
            cls.set_logger(opts['logger'])
        if 'slash_character' in opts:
            cls.set_slash_character(opts['slash_character'])
        if 'cache_dir' in opts:
            cls.set_cache_dir(opts['cache_dir'])

    @classmethod
    def set_logger(cls, logger):
        cls._logger = logger

    @classmethod
    def set_slash_character(cls, slash_character):
        cls._slash_char = slash_character

    @classmethod
    def set_cache_dir(cls, cache_dir):
        cls._cache_dir = cache_dir

    # Utilities to read the cache

    @classmethod
    def get_cache_path(cls, url):
        return os.path.join(cls._cache_dir, url.replace('/',cls._slash_char))

    @classmethod
    def has_cached(cls, url):
        return os.path.isfile(cls.get_cache_path(url))

    @classmethod
    def get_cached(cls, url):
        cache_path = cls.get_cache_path(url)
        cls._logger.debug("Getting url from cache at %s" % cache_path)
        infile = codecs.open(cls.get_cache_path(url), 'r', 'utf-8')
        html = infile.read()
        infile.close()
        return html

    @classmethod
    def put_cached(cls, url, html):
        cache_path = cls.get_cache_path(url)
        cls._logger.debug("Putting url to cache at %s" % cache_path)
        outfile = codecs.open(cache_path, 'w', 'utf-8')
        outfile.write(html)
        outfile.close()

    @classmethod
    def _read_url(cls, url):
        cls._logger.debug("Reading url %s" % url)
        usock = _opener.open(url)
        html = unicode(usock.read(), 'utf-8')
        usock.close()
        return html

    # Method that gets the html of a url, from cache if available

    @classmethod
    def read_url(cls, url, redownload=False):
        if cls.has_cached(url) and not redownload:
            return cls.get_cached(url)

        html = cls._read_url(url)
        cls.put_cached(url, html)
        return html

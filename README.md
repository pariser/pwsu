# Python Web Scraping Utilities (PWSU)

pariser/pwsu on Github (http://github.com/pariser/pwsu)
Written by Andrew Pariser [ http://pariser.me / @pariser]

## Provides the following tools

- HTMLCache

## About HTMLCache

The goal of HTMLCache is to locally cache the HTML from a live URL, so that
while writing a web scraping tool, you reduce the number of live calls to the
server.

#### Usage

The goal is to make the library as easy to use as possible. To download the
html for a given url and cache the result (or read the cached version, if it
exists), run:

    html = HTMLCache.read_url(url, redownload=False)

#### Configuration

Use the following methods to set options that affect library behavior

    HTMLCache.set_logger( logger )
    HTMLCache.set_cache_dir( cache_dir )
    HTMLCache.set_slash_character( slash_character )

- *logger* is an override of a default Python logger, which prints DEBUG
  messages regarding the operation of the HTMLCache.
- *cache_dir* defines the folder into which html files are cached. Its default
  value is '~/data/html_cache'.
- *slash_character* is used to to replace slashes in the output file name. Its
  default value is '~', so that

    URL: http://github.com/pariser/pwsu 
    CACHE FILE: cache_dir + "/http:~~github.com~pariser~pwsu"

A convenience method allows setting all options at once:

    HTMLCache.set_opts( opts={} )

where opts is a dictionary with optional keys 'logger', 'cache_dir', and
'slash_character'.


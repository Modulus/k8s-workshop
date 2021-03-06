#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'John Sigvald Skauge'
SITENAME = 'k8s-workshop'
SITEURL = ''
PATH = 'content'

TIMEZONE = 'Europe/Oslo'

DISPLAY_CATEGORIES_ON_MENU = False
DEFAULT_LANG = 'no'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

STATIC_PATHS = ["images"]

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = False
#THEME = "/Users/johnsigvaldskauge/pelican-themes/html5-dopetrope"

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = 'justin cai'
SITENAME = 'justin cai'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'America/Denver'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'https://getpelican.com/'),
         ('Python.org', 'https://www.python.org/'),
         ('Jinja2', 'https://palletsprojects.com/p/jinja/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

THEME = "theme"

# index refers to the list of all blog posts, not site index
INDEX_SAVE_AS = "blog.html"

PLUGINS = [
    # server side rendering of katex math
    "pelican_katex",
    # for generating sitemap
    "sitemap",
]

ARTICLE_URL = "blog/{date:%Y}/{date:%m}/{date:%d}/{slug}"
ARTICLE_SAVE_AS = ARTICLE_URL + "/index.html"

# settings these to "" removes the default behavior
# of generating these pages
CATEGORY_SAVE_AS = ""
CATEGORIES_SAVE_AS = ""
TAGS_SAVE_AS = ""
AUTHOR_SAVE_AS = ""
AUTHORS_SAVE_AS = ""
ARCHIVES_SAVE_AS = ""

# these options will copy the CNAME file into the
# base of the output directory 
STATIC_PATHS = ["static/CNAME"]
EXTRA_PATH_METADATA = {"static/CNAME": {"path": "CNAME"}}

# regex to extract date and slug
FILENAME_METADATA = r'(?P<date>\d{4}-\d{2}-\d{2})-(?P<slug>.*)'

SITEMAP = {"format": "xml"}

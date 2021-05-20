#!/usr/bin/env pythonb
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
INDEX_SAVE_AS = "blog.html"
PLUGINS = ["pelican_katex", "sitemap"]
ARTICLE_URL = "blog/{date:%Y}/{date:%m}/{date:%d}/{slug}"
ARTICLE_SAVE_AS = "blog/{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html"
CATEGORY_SAVE_AS = ""
CATEGORIES_SAVE_AS = ""
TAG_SAVE_AS = ""
TAGS_SAVE_AS = ""
AUTHOR_SAVE_AS = ""
AUTHORS_SAVE_AS = ""
ARCHIVES_SAVE_AS = ""
STATIC_PATHS = ["static/CNAME"]
EXTRA_PATH_METADATA = {"static/CNAME": {"path": "CNAME"}}
# DOCUTILS_SETTINGS = {
#     "writer": "html5"
# }
FILENAME_METADATA = r'(?P<date>\d{4}-\d{2}-\d{2})-(?P<slug>.*)'
SITEMAP = {"format": "xml"}

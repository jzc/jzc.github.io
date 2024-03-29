#!/usr/bin/env python
# -*- coding: utf-8 -*- #

# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys
sys.path.append(os.curdir)
from pelicanconf import *

# If your site is available via HTTPS, make sure SITEURL begins with https://
SITEURL = 'https://justincai.com'
RELATIVE_URLS = False

# FEED_ALL_ATOM = 'feeds/all.atom.xml'
# CATEGORY_FEED_ATOM = 'feeds/{slug}.atom.xml'

# clean before making files
DELETE_OUTPUT_DIRECTORY = True

# this makes it so drafts do not appear
DRAFT_SAVE_AS = ""

# Following items are often useful when publishing

#DISQUS_SITENAME = ""
#GOOGLE_ANALYTICS = ""

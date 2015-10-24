#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys
sys.path.append(os.curdir)
from pelicanconf import *

SITEURL = 'http://rajalokan.github.io'
FAVICON = SITEURL + '/images/favicon.ico'
RELATIVE_URLS = False

OUTPUT_PATH = '../rajalokan.github.io/'
FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/%s.atom.xml'

DELETE_OUTPUT_DIRECTORY = True

# Following items are often useful when publishing

DISQUS_SITENAME = "rajalokan"
GOOGLE_ANALYTICS = "rajalokan"
ADD_THIS_ID = 'ra-55adbb025d4f7e55'

USE_LESS = False

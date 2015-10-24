#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Alok Kumar'
SITEURL = u'http://localhost:8000'
SITENAME = u'@rajalokan'
SITETITLE = AUTHOR
SITESUBTITLE = u'Works at @aptira. Django, python, openstack, ansible. Married to @gudia1ta. Bangalore'
SITEDESCRIPTION = u'%s\'s Random thoughts' % AUTHOR
SITELOGO = u'https://pbs.twimg.com/profile_images/602902686636187648/0_aZ0JrS_400x400.jpg'
FAVICON = SITEURL + '/images/favicon.ico'

#ROBOTS = u'index, follow'

THEME='../flex'
OUTPUT_PATH = '../rajalokan.github.local/'
OUTPUT_RETENTION = ['.git']
PATH = 'content'
TIMEZONE = 'Asia/Kolkata'
DEFAULT_LANG = 'en'
OG_LOCALE = u'en_US'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

USE_FOLDER_AS_CATEGORY = True
#MAIN_MENU = False

LINKS = (('About me', 'http://rajalokan.com/'),)

# Social widget
SOCIAL = (('linkedin', 'https://in.linkedin.com/pub/alok-kumar/8/b83/947'),
          ('github', 'https://github.com/rajalokan'),
          ('twitter', 'https://twitter.com/rajalokan'),
          ('google', 'https://plus.google.com/u/0/113206559731694133262/posts'),)

#MENUITEMS = (('Archives', '/archives.html'),
#             ('Categories', '/categories.html'),
#             ('Tags', '/tags.html'),)
#
CC_LICENSE = {
            'name': 'Creative Commons Attribution-ShareAlike',
            'version': '4.0',
            'slug': 'by-sa'
}

COPYRIGHT_YEAR = 2015

DEFAULT_PAGINATION = 5

#PLUGIN_PATHS = ['./pelican-plugins']
#PLUGINS = ['sitemap']
#
#SITEMAP = {
#    'format': 'xml',
#    'priorities': {
#        'articles': 0.6,
#        'indexes': 0.6,
#        'pages': 0.5
#    },
#        'changefreqs': {
#        'articles': 'monthly',
#        'indexes': 'daily',
#        'pages': 'monthly'
#    }
#}
#
#STATUSCAKE = {
#    'trackid': 'SL0UAgrsYP',
#    'days': 7
#}
#
USE_LESS = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

#COVER_IMG_URL='http://graviton.co.in/wp-content/uploads/2013/08/python-logo.jpg'
#COVER_IMG_URL='http://i.stack.imgur.com/oSyyX.png'

#LINKEDIN_URL='rajalokan'
#TWITTER_URL='rajalokan'
#GITHUB_URL='rajalokan'

DISQUS_SITENAME='rajalokan'

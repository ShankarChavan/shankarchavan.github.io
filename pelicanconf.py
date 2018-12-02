#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Shankar'
SITENAME = 'Understanding Unexplained'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Asia/Kolkata'

DEFAULT_LANG = 'en'

HEADER_COLOR = 'black'
#css file
COLOR_SCHEME_CSS = 'github_jekyll.css'


# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('github', 'http://github.com/shankarchavan'),
          ('linkedin', 'http://www.linkedin.com/in/shankar-chavan-15852842'),)

DEFAULT_PAGINATION = 10
THEME = './Pelican-themes/clean/pelican-clean-blog'
#THEME = './Pelican-themes/elegant'

IGNORE_FILES = ['.ipynb_checkpoints']
MARKUP = ('md', 'ipynb')


PLUGIN_PATHS = ['./plugins']
PLUGINS = ['ipynb.markup']
# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

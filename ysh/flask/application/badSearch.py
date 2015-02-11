#-*- coding: utf-8 -*-


import requests
from BeautifulSoup import BeautifulSoup as bs
import sys
from xml.etree.ElementTree import parse

import re


def badResult(query):

	baseUrl = 'http://openapi.naver.com/search?key=021baa459c36eb3a11b53bdde1b32538&display=100&start=1&target=blog&sort=sim&'+urllib.urlencode({'query':query+' 별로'})
	dump = parse(urllib2.urlopen(baseUrl)).getroot()
	result = list()

	pat = re.compile('(<script(\s|\S)*?<\/script>)|(<style(\s|\S)*?<\/style>)|(<!--(\s|\S)*?-->)|(<\/?(\s|\S)*?>)')
	for  li in dump.getiterator('description'):
		PatternString = pat.sub('',"".join(li.text.split('...')))
		result.append(PatternString)
	return result







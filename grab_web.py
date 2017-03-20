#!/usr/bin/python
# -*- coding:utf-8 -*-

import urllib
import urllib2
import re

def get_image(url):
  reg = re.compile(r'img.src="(.*?)"')
  res = re.findall(reg, url)
  count = 0
  for data in res:
    count += 1
    urllib.urlretrieve(data, '%s.jpg'%count)

if __name__ == '__main__':
  user_input_url = raw_input('input url:')
  open_url = urllib2.urlopen(user_input_url)
  read_url = open_url.read()
  get_image(read_url)
#!/usr/bin/python
# -*- coding:utf-8 -*-

from urllib import urlretrieve

def first_non_blank(lines):
    for eachline in lines:
        if not eachline.strip():
            continue
        else:
            return eachline

def first_last(webpage):
   f = open(webpage)
   lines = f.readlines()
   f.close()
   print first_non_blank(lines)
   lines.reverse()
   print first_non_blank(lines)

def download(url = 'http://www', process = first_non_blank):
    try:
        retval = urlretrieve(url)[0]
    except IOError:
        retval = None
    if retval:
        process(retval)

if __name__ == '__main__':
    download()

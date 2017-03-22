#!/usr/bin/python
# -*- coding:utf8 -*-

import os
import sys

# def map_func(x):
#     return x+2
    
def reduce_func(x, y):
    return x*10 + y

if __name__ == '__main__':
    init_list = [2, 4, 5, 6]
    map_list = map((lambda x:x+2), init_list)
    print 'map_list is:', map_list
    reduce_res = reduce(reduce_func, map_list)
    print 'reduce_res is:', reduce_res

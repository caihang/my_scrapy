#!/usr/bin/python
# -*- coding:utf8 -*-

def foo(arg1, arg2, *arg3, **arg4):
    print 'arg1 is:', arg1
    print 'arg2 is:', arg2
    loop = 0
    for arg in arg3:
        print 'arg3[%d] arg is %s:'%(loop, arg)
        loop += 1
    loop = 0
    for key in arg4:
        print '[%d]--%s:%s'%(loop, key, arg4[key])
        loop += 1

if __name__ == '__main__':
    a_tupe = (3, 4, 5)
    a_dict = {"name":"caicai", "age":"11"}
    foo('2017/3/20', 'Monday', 2, sex = 'male', *a_tupe, **a_dict)
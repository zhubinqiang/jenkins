#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# **********************************************
# @file: build1.py
# @author: ZhuBinQiang <zhu.binqiang@163.com>
# @create time: 2018-03-25 23:04:49
# @last modified: 2018-03-25 23:16:00
# @description:
# **********************************************

import os

def main():
    for i in range(1, 10):
        for j in range(1, i+1):
            print("%d * %d = %d\t" %(j, i, i*j)),
        print("")

if __name__  == '__main__':
    main()

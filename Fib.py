#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Fib 序列
#两个元素的值定义下一个

a, b = 0, 1
while b < 10: 
    print b,  # 输出不换行，并且以空格分隔
    a, b = b, a+b


```python
#####################################################
#	File Name: _decorate_bubble.py
#	Author: Rachel Liu
#	Created Time: 2017-04-13
#	Description: create the bubble list and decorate it,
#				dedupe the list and find the odd element
#	Modified History: 
#	
#	Copyright (C)2017 All Rights Reserved
#####################################################
#!/usr/bin/env python
#-*- coding:utf-8 -*-

import random
import functools


def dec_odd(func): # 返回传入列表 seq的odd element 列表
    @functools.wraps(func)
    def wrapper(seq):
        seq = func(seq)
        odd_seq = [i for i in seq if i%2==1]
        print ("odd_seq:{
0}".format(odd_seq))
        return odd_seq
    return wrapper

def dec_distinct(func): # 返回传入列表 seq 排序后dedupe 的列表
    @functools.wraps(func)
    def wrapper(seq):
        seq = func(seq)
        s = list(set(seq))
        print ("distinct_seq:{
0}".format(s))
        return s
    return wrapper

@dec_odd
@dec_distinct
def sort_bubble(seq): # 返回传入列表 seq 排序后的列表
    s = seq
    for i in range(len(s)):
        for j in range(i + 1, len(s)):
            if s[j] < s[i]:
                (s[i], s[j]) = (s[j], s[i])
    print ("bubble_seq:{
0}".format(s))
    return s

def gen_random_seq(length):
    l=length
    seq = []
    while l > 0:
        seq.append(random.randrange(10))
        l = l - 1
    return seq
   # seq = random.sample(range(10000),l)
    return seq

r_seq = gen_random_seq(6)
print ("origin_seq:{
0}".format(r_seq))

sort_seq = sort_bubble(r_seq)
#
# origin_seq:[8, 7, 5, 2, 2, 4]
# bubble_seq:[2, 2, 4, 5, 7, 8]
# distinct_seq:[8, 2, 4, 5, 7]
# odd_seq:[8, 2, 4]
```

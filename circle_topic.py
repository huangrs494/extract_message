#  -*- coding:utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import re

circle_msg = open(u"E:/pycharm_project/important_msg/circle/tt_circle_msg.txt")
cir = circle_msg.readlines()
#!/usr/bin/env python
#encoding: utf-8
import sys
default_encoding = 'utf-8'
if sys.getdefaultencoding() != default_encoding:
    reload(sys)
    sys.setdefaultencoding(default_encoding)
topic = open(u"E:/pycharm_project/important_msg/circle/topic.txt")

top = topic.readlines()
top[0] = top[0].replace('\xef\xbb\xbf', '')
'''
#print top
for t in top:
    print t,len(t)
'''
circle_topic = open(u"E:/pycharm_project/important_msg/circle/circle_topic.txt",'w')

for t in top:
    #print 'ttt',t
    #t = re.sub('','\t',t)
    t = t.strip()
    #print t, len(t)
    for c in cir:
        #print  c
        if t in c:
            #print 'ccccc',c,'tttt',t
            circle_topic.write(t)
            circle_topic.write('\t')
            circle_topic.write(c)
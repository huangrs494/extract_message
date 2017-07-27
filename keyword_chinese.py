#  -*- coding:utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import re
import jieba.analyse
#导入自定义词典
jieba.load_userdict("E:/pycharm_project/important_msg/circle/dict.txt")
#载入语料
chinese_contents = open(u"C:/......txt")
contents = chinese_contents.readlines()

#写入关键词信息
join_user_topic = open(u"C:/.....关键词.txt",'w')
#print len(contents)
#print '77111',contents
#读取消息内容列，对固定列，过滤数字和英文信息，提取中文信息并提取关键词
for i in contents:
    content_list = i.replace('#', '').replace('一一', '').strip('\n').split('\t')
    chinese_content = ''.join(x for x in unicode(content_list[2]) if ord(x) >= 256)

    key_content = jieba.analyse.extract_tags(chinese_content, topK=5, withWeight=False)
    join_user_topic.write('\n')
    join_user_topic.write(u"{}\t{}\t{}\t".format(content_list[0], content_list[1], content_list[2]))
    for j in key_content:
        # if ord(int(i)) < 256:
        #     continue
        join_user_topic.write(u"{}\t".format(j))

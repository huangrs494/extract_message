#  -*- coding:utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import jieba.analyse
#导入自定义词典
jieba.load_userdict("E:/pycharm_project/important_msg/circle/dict.txt")

#导入需要计算的内容
chinese_contents = open(u"C:/.....chinese_contents.txt")
neirong = chinese_contents.read()
zidian={}
fenci=jieba.cut_for_search(neirong)   #搜索引擎模式分词
for fc in fenci:
        if fc in zidian:
                zidian[fc]+=1           #字典中如果存在键，键值加1，
        else:
                zidian.setdefault(fc,1)   #字典中如果不存在键，就加入键，键值设置为1
quanzhong=jieba.analyse.extract_tags(neirong,topK=50)       #计算tf-idf，输出前20的权重词。
for qg in quanzhong:                                     #不存在的话就输出qg和出现qg的次数
                print qg+`zidian[qg]`       #输出权重词和权重词出现的次数


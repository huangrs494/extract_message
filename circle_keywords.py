#!/usr/bin/env python
#encoding: utf-8
import sys
default_encoding = 'utf-8'
if sys.getdefaultencoding() != default_encoding:
    reload(sys)
    sys.setdefaultencoding(default_encoding)
#上面为设置默认编码
import jieba
import jieba.analyse
#导入自定义词典
jieba.load_userdict("E:/pycharm_project/important_msg/circle/dict.txt")


#jieba.analyse.set_stop_words("E:/pycharm_project/important_msg/circle/stop.txt")
#载入语料
circle_topic = open(u"E:/pycharm_project/important_msg/circle/circle_topic_test.txt")
cirtop = circle_topic.readlines()
cirtop[0] = cirtop[0].replace('\xef\xbb\xbf', '')

#写入合并同一个用户，同一个话题的消息内容。写入内容和关键词
join_user_topic = open(u"E:/pycharm_project/important_msg/circle/join_user_topic_test1_test.txt",'w')
keywords_user_topic = open(u"E:/pycharm_project/important_msg/circle/keywords_user_topic_test.txt",'w')
usr_list = []
for inx,i in enumerate(cirtop):
    #print i
    circle_topic_list = i.strip('\n').split('\t')
    topic_name = circle_topic_list[0]
    useid = circle_topic_list[1]
    circle_content = circle_topic_list[2]
    #删除content里面的话题内容
    if topic_name in circle_content:
        #print circle_content
        circle_topic_list[2] = circle_content.replace(topic_name,'').replace('#','')
    #print 'cccc',circle_content
    usr_list.append(circle_topic_list)
#print '111',len(usr_list[0][0])


i = -1
#合并同一个用户同一个话题的消息内容
newlist = []
index_list = []
while usr_list:
    new_usr_list = []
    i = i + 1
    newlist.append(usr_list.pop())
    for k in range(len(usr_list)):
        if newlist[i][0] == usr_list[k][0] and newlist[i][1] == usr_list[k][1]:
            newlist[i][2] = newlist[i][2] + usr_list[k][2]
            #del usr_list[k]
            #print k
            index_list.append(k)
    #print index_list
    for j in range(len(usr_list)):
        #print 'j',j
        if j not in index_list:
            #print 'i',j
            new_usr_list.append(usr_list[j])
    #print len(new_usr_list)
    usr_list = new_usr_list

    #提取关键词
    #print len(newlist[i][2])
    if len(newlist[i][2]) == 1:
        newlist[i][2] = newlist[i][0]
        #print newlist[i][2]
    print 'zzz', newlist[i][2]
    join_user_topic.write(u"{}\t{}\t{}\r\n".format(newlist[i][0], newlist[i][1], newlist[i][2]))

    keywords_user_topic.write(u"{}\t{}\t{}".format(newlist[i][0], newlist[i][1], newlist[i][2]))

    key_content = jieba.analyse.extract_tags(newlist[i][2], topK=10, withWeight=False)
    print key_content
    key_content.remove('艾艾贴')
    print key_content


    # key_content = jieba.analyse.extract_tags(newlist[i][2], topK=10,withWeight = True)
    # #print key_content[0][0].decode('utf-8')
    # for k,w in key_content:
    #     #print 'k',k,'w',w
    #     #print key_content
    #     if k == '艾艾贴':
    #         continue
    #     keywords_user_topic.write('\t')
    #     keywords_user_topic.write(k)
    #     keywords_user_topic.write('\t')
    #     w = str(w)
    #     keywords_user_topic.write(w)
    # keywords_user_topic.write('\n')
    #print 'nk', k, 'w', w


# ul_len = len(usr_list)
# for i in range(ul_len):
#     newlist.append(usr_list.pop())
#     j = j + 1
    # for k in range(len(usr_list)):
    #     if newlist[j][0] == usr_list[k][0] and newlist[j][1] == usr_list[k][1]:
    #         #删除usrlist里面相同的（usrlist[k]）
    #         print 'ww',usr_list[k][2]
    #         #print 'www',usr_list[][2]
    #         newlist[j][2] = newlist[j][2] + usr_list[k][2]
    #         print '1', newlist[j][0], '2', usr_list[k][0]
    #         print '11', newlist[j][1], '22', usr_list[k][1]
    #         print '111',newlist[j][2],'222',usr_list[k][2]
    #         del usr_list[k]


    # for usrlist in usr_list:
    #     if newlist[j][0] == usrlist[0] and newlist[j][1] == usrlist[1]:
    #         newlist[j][2] = newlist[j][2] + usrlist[2]
    #         #del usrlist
    # print 'zzz', newlist[i][2]

# for i in range(len(newlist)):
#     print newlist[i][1]
#     print 'zzz',newlist[i][2]
#


# for urlt in usr_list:
#     #print type(urlt)
#     new_usr_list = usr_list.pop()
#     #print urlt[0]
#     print new_usr_list[0]
#     for i in range(len(new_usr_list)):
#
#         print 'ur',urlt[0],'new',new_usr_list[i][0]
#         if urlt[0] == new_usr_list[i][0]:
#             print 'aaaa',new_usr_list[i][2]



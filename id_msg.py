#  -*- coding:utf-8 -*-

import os
import csv
import codecs




new_file = u"E:/pycharm_project/important_msg/抽取的数据/tt_circle_msg.txt"
#五月份的数据转换成txt:
if os.path.exists(new_file):
    os.remove(new_file)
with codecs.open(new_file, "a", "utf-8") as fw:
    #print "55555"
    with open(u"E:/pycharm_project/important_msg/抽取的数据/tt_circle.csv", 'rb') as csv_file:
        csv_reader = csv.reader(csv_file)
        try:  # _csv.Error: line contains NULL byte
            for row in csv_reader:

                data = row[2].decode("utf-8", "ignore").strip().replace("\n", " ")
                print data
                fw.write(u"{}\t{}\r\n".format(row[1].decode("utf-8", "ignore").strip(),data.strip().replace("\\n", " ")))
        except csv.Error, e:
            print 'file %s: %s' % (new_file, e)


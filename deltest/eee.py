# -*- coding: utf-8 -*-

import os
import re
pswpath = open("aa.txt",'r')
fbread = pswpath.readlines()
fspath= open("cc.txt",'r')
fsread = fspath.readlines()
#print(fsread)

tmppath = "bb.txt"
tmp_file = open(tmppath, "w")
# f = open(pswpath, "r")
# lines = f.readlines()
# for line in lines:
#     if line.find('最后') > -1:
#         print(line.find('最后'))
#         continue
#     tmp_file.write(line)
# f.close()
#
# tmp_file.close()

# for line in open(pswpath):
#         if re.match('最后', line):
#             print(line[:-1])
#             print(line)
#             continue
#         tmp_file.write(line)
# tmp_file.close()
f_del = []
f_save = []
for inx,line in enumerate(fbread):
    line = line.strip('\n')
    print('lll',line)
    for s in fsread:
        s = s.strip('\n')
        print(s)
        if re.findall(s, line):
            #print(re.compile('最后', line))
            f_del.append(inx)
            print(line)
            continue

    print('xieru',line,f_del)


for inx,line in enumerate(fbread):
    if inx in f_del:
        continue
    else:
        print('haole',line)
        tmp_file.write(line)
print('www',f_del)
tmp_file.close()
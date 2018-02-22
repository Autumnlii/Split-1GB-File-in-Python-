#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 26 12:35:17 2017

@author: qiuying
"""

import os


filePath = 'source.csv.gz'
filebig = os.path.getsize(filePath)
fp_r = open(filePath,'rb')  #the file read in

each_file = filebig // 10 #split total file, each piece big
total_read = 0
for i in  range(1,10):  #the first nine pieces
    fp_w = open('{}.csv.gz'.format(i),'wb')
    
    each_len = 0
    while each_len < each_file:
        #rewrite each one
        data = fp_r.read(1024)
        each_len += len(data)
        fp_w.write(data)
    total_read += each_len
    fp_w.close()

fp_w = open('10.csv.gz','wb')
each_len = 0
#the 10th  one
while each_len < filebig - total_read:
        
    data = fp_r.read(1024)
    each_len += len(data)
    fp_w.write(data)

fp_w.close()  #close the handle
fp_r.close()

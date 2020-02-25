from datasketch import MinHash
import re
from string import punctuation
import pandas as pd
import os
import csv

csv_data1 = pd.read_csv(filepath_or_buffer=os.path.dirname(__file__)+'/Amazon.csv',
                           header=None, encoding='windows-1252')  # 读取训练数据
traindata1 = csv_data1[1]

csv_data1 = csv_data1.fillna(value='')
"""
traindata1 = ''
for row1 in csv_data1:
    if row1==0:
        continue
    elif row1==1:
        traindata1 = csv_data1[row1]
    else:
        traindata1 = traindata1 + ' ' + csv_data1[row1]
"""
csv_data2 = pd.read_csv(filepath_or_buffer=os.path.dirname(__file__)+'/Google.csv',
                           header=None, encoding='windows-1252')  # 读取训练数据

csv_data2 = csv_data2.fillna(value='')
traindata2 = csv_data2[1]
"""
traindata2 = ''
for row2 in csv_data2:
    if row2==0:
        continue
    elif row2==1:
        traindata2 = csv_data2[row2]
    else:
        traindata2 = traindata2 + ' ' + csv_data2[row2]
#print(len(csv_data2.index))
#print(csv_data2.loc[1, 0])
"""
maxhash = ['', '', 0]

with open('./a-g.csv', 'a') as file:
    writer = csv.writer(file)
    writer.writerow(["amazon", "google"])
    m = [MinHash() for i1 in range(2)]
    for j in range(1, len(csv_data1.index)):
        t2 = re.sub(r"[%s]+" % punctuation, "", traindata1[j])
        t2c = t2.strip().split()
        for p2 in t2c:
            m[1].update(p2.encode('utf8'))
        for i in range(1, len(csv_data2.index)):
            t1 = re.sub(r"[%s]+" % punctuation, "", traindata2[i])
            t1c = t1.strip().split()
            for p1 in t1c:
                m[0].update(p1.encode('utf8'))
            c = m[1].jaccard(m[0])
            if c == maxhash[2] and c != 0:
                maxhash.append(csv_data1.loc[j, 0])
                maxhash.append(csv_data2.loc[i, 0])
                maxhash.append(c)
            if c > maxhash[2]:
                if len(maxhash)>3:
                    maxhash = ['', '', 0]
                maxhash[0] = csv_data1.loc[j, 0]
                maxhash[1] = csv_data2.loc[i, 0]
                maxhash[2] = c
            #print(maxhash)
            m[0]=MinHash()
        # 写入多行用writerows
        if len(maxhash) > 3:
            for bn in range(len(maxhash)):
                if bn % 3 == 0:
                    writer.writerows([[maxhash[bn], maxhash[bn+1]]])
        else:
            writer.writerows([[maxhash[0], maxhash[1]]])
        m[1]=MinHash()
        maxhash = ['', '', 0]


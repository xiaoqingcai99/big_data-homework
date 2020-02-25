from datasketch import MinHash
import re
from string import punctuation
import csv

amazon = []
google = []

with open('./amazon-titles.txt', encoding='windows-1252') as fa:
    for pp in fa.readlines():
        pp = pp.strip('\n')
        amazon.append(pp)



with open('./google-names.txt', encoding='windows-1252') as fg:
    for qq in fg.readlines():
        qq = qq.strip('\n')
        google.append(qq)


maxhash = ['', '', 0]

with open('./title_match.csv', 'a') as file:
    writer = csv.writer(file)
    m = [MinHash() for i1 in range(2)]
    for j in range(1, len(amazon)):
        t2 = re.sub(r"[%s]+" % punctuation, "", amazon[j])
        t2 = t2.replace('\n', '')
        t2c = t2.strip().split()
        for p2 in t2c:
            m[1].update(p2.encode('utf8'))
        for i in range(1, len(google)):
            t1 = re.sub(r"[%s]+" % punctuation, "", google[i])
            t1 = t1.replace('\n', '')
            t1c = t1.strip().split()
            for p1 in t1c:
                m[0].update(p1.encode('utf8'))
            c = m[1].jaccard(m[0])
            if c == maxhash[2] and c != 0:
                maxhash.append(amazon[j])
                maxhash.append(google[i])
                maxhash.append(c)
            if c > maxhash[2]:
                if len(maxhash)>3:
                    maxhash = ['', '', 0]
                maxhash[0] = amazon[j]
                maxhash[1] = google[i]
                maxhash[2] = c
            #print(maxhash)
            m[0] = MinHash()
        # 写入多行用writerows
        if len(maxhash) > 3:
            for bn in range(len(maxhash)):
                if bn % 3 == 0:
                    writer.writerows([[maxhash[bn], maxhash[bn+1]]])
        else:
            writer.writerows([[maxhash[0], maxhash[1]]])
        m[1]=MinHash()
        maxhash = ['', '', 0]


"""

m1, m2 = MinHash(), MinHash()
for d in aa:
    m1.update(d.encode('utf8'))
for d in gg:
    m2.update(d.encode('utf8'))
print("估计Jaccard相似度：", m1.jaccard(m2))


s1 = set(aa)
s2 = set(gg)
actual_jaccard = float(len(s1.intersection(s2)))/float(len(s1.union(s2)))
print("真实Jaccard相似度：", actual_jaccard)
"""

from apyori import *
import pandas as pd
import os

csv_data = pd.read_csv(filepath_or_buffer=os.path.dirname(__file__)+'/sales_detail1.csv',
                           header=None)  # 读取训练数据
train_batch_data = csv_data[0]
order_num = ''
fin_list = []
count = 0

for i in range(len(train_batch_data)):
    z = train_batch_data[i].split(' ')
    # 去除不是正规商品集(2行)
    if len(z) != 2:
        continue
    if order_num == z[0].split('\t')[0]:
        order_num = z[0].split('\t')[0]
        products_name = z[1].split('\t')[3]
        fin_list[count].append(products_name)
    else:
        order_num = z[0].split('\t')[0]
        products_name = z[1].split('\t')[3]
        tem_list = [products_name]
        fin_list.append(tem_list)
        if i != 0:
            count += 1


result = list(apriori(fin_list, min_support=0.001, min_confidence=0.01, min_length=1))

for rule in result:
    print(rule)
print("共有%d个频繁项集"%len(result))


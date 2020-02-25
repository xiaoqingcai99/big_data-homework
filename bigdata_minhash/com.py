import pandas as pd
import os


csv_data1 = pd.read_csv(filepath_or_buffer=os.path.dirname(__file__)+'/a-g.csv',
                           header=None, encoding='windows-1252')  # 读取训练数据

csv_data2 = pd.read_csv(filepath_or_buffer=os.path.dirname(__file__)+'/Amazon_Google_perfectMapping.csv',
                           header=None, encoding='windows-1252')  # 读取训练数据


correct = 0
wrong = 0

for i in range(1, len(csv_data1)):
    print(i)
    count = 0
    for j in range(1,len(csv_data2)):
        if csv_data1.loc[i, 0]==csv_data2.loc[j, 0]:
            if csv_data1.loc[i, 1]==csv_data2.loc[j, 1]:
                correct += 1
                count += 1
                break
            elif count==0:
                wrong += 1
    count=0

print('correct: %s, wrong: %s' %(str(correct), str(wrong)))
pe = round(correct/(correct+wrong), 2 )
print(pe)

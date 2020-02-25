import Levenshtein
import numpy as np
import string
import pandas as pd
import os
import sklearn
from sklearn.cluster import KMeans


def distEclud(strA, strB):#计算两个词的编辑距离
    a = Levenshtein.distance(strA, strB)
    return a


def read_file():
    csv_data = pd.read_csv(filepath_or_buffer=os.path.dirname(__file__) + '/sales_detail1.csv',
                               header=None)  # 读取训练数据
    train_batch_data = csv_data[0]

    for i in range(len(train_batch_data)):
        if i >1500:
            break
        z = train_batch_data[i].split(' ')
        # 去除不是正规商品集(2行)
        if len(z) != 2:
            continue
        products_name = z[1].split('\t')[3]
        products_set.add(products_name)


    """
    def randCent(dataSet, k):#随机质心
        n = np.shape(dataSet)[1]
        centroids = np.mat(np.zeros((k, n)))
        for j in range(n):
            minJ = min(dataSet[:,j])
            rangeJ = float(max(dataSet[:,j]) - minJ)
            centroids[:,j] = np.mat(minJ + rangeJ * np.random.rand(k,1))
        return centroids
    
    
    def KMeans(dataSet, k):
        m = np.shape(dataSet)[0]  # 行的数目
        # 第一列存样本属于哪一簇
        # 第二列存样本的到簇的中心点的误差
        clusterAssment = np.mat(np.zeros((m, 2)))
        clusterChange = True
    
        # 第1步 初始化centroids
        centroids = randCent(dataSet, k)
        while clusterChange:
            clusterChange = False
    
            # 遍历所有的样本（行数）
            for i in range(m):
                minDist = 100000.0
                minIndex = -1
    
                # 遍历所有的质心
                # 第2步 找出最近的质心
                for j in range(k):
                    # 计算该样本到质心的欧式距离
                    distance = distEclud(centroids[j, :], dataSet[i, :])
                    if distance < minDist:
                        minDist = distance
                        minIndex = j
                # 第 3 步：更新每一行样本所属的簇
                if clusterAssment[i, 0] != minIndex:
                    clusterChange = True
                    clusterAssment[i, :] = minIndex, minDist ** 2
            # 第 4 步：更新质心
            for j in range(k):
                pointsInCluster = dataSet[np.nonzero(clusterAssment[:, 0].A == j)[0]]  # 获取簇类所有的点
                centroids[j, :] = np.mean(pointsInCluster, axis=0)  # 对矩阵的行求均值
    
        print("Congratulations,cluster complete!")
        return centroids, clusterAssment
    """

def main(dataset,k):
    words = list(products_set)
    words = np.asarray(words)


    lev_similarity = -1 * np.array([[dataset(w1, w2) for w1 in words] for w2 in words])

    affprop = sklearn.cluster.AffinityPropagation(affinity="precomputed", damping=0.5)
    affprop.fit(lev_similarity)
    ap_file = open('.1.txt', 'w')

    for cluster_id in np.unique(affprop.labels_):
        exemplar = words[affprop.cluster_centers_indices_[cluster_id]]
        cluster = np.unique(words[np.nonzero(affprop.labels_ == cluster_id)])
        cluster_str = ", ".join(cluster)
        print(" - *%s:* %s \n" % (exemplar, cluster_str))
        ap_file.write(" - *%s:* %s \n" % (exemplar, cluster_str))

    ap_file.close()


if __name__ == '__main__':
    products_set = set()
    read_file()
    pro = {}
    k = 12
    testtest()

    #centroids, clusterAssment = KMeans(products_set, k)


# This Python file uses the following encoding: utf-8


import numpy as np
import sklearn.cluster
import Levenshtein
import string



def Edistance(w1, w2):
    if len(w1) > len(w2):
        return Levenshtein.distance(w1, w2) * 100 / len(w1)
    elif len(w2)!=0:
        return Levenshtein.distance(w1, w2) * 100 / len(w2)


products = set()

with open('./sales_detail1.csv', 'r+', encoding='utf-8') as sales_detail_raw:
    sales_details = sales_detail_raw.readlines()
    count = 0
    for line in sales_details:
        if count>1500:
            break
        line = line.replace('"', '').split("\t")[5]
        pro = line.translate(str.maketrans('', '', string.punctuation))
        pro = pro.translate(str.maketrans('', '', string.digits))
        pro = pro.translate(str.maketrans('', '', string.ascii_letters))
        products.add(pro)
        count+=1


pp = list(products)
prod_n = np.asarray(pp)


similarity = (-1) * np.array([[Edistance(w1, w2) for w1 in prod_n] for w2 in prod_n])



ap = sklearn.cluster.AffinityPropagation(affinity="precomputed", damping=0.5)
ap.fit(similarity)


with open('1.txt', 'w') as f:
    for cluster_id in np.unique(ap.labels_):
        exemplar = prod_n[ap.cluster_centers_indices_[cluster_id]]
        cluster = np.unique(prod_n[np.nonzero(ap.labels_ == cluster_id)])
        cluster_str = ", ".join(cluster)
        print(" - %s:  %s \n" % (exemplar, cluster_str))
        f.write(" - %s: %s \n" % (exemplar, cluster_str))


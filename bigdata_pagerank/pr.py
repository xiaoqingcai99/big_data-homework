import networkx as nx

G = nx.DiGraph()
with open('./web-Google.txt') as file:
    for line in file:
        if '#' in line:
            continue
        head, tail = [int(x) for x in line.split('\t')]
        G.add_edge(head, tail)
        #print(head)
pr = nx.pagerank(G, alpha=0.85)

z = sorted(pr.items(), key=lambda x: x[1], reverse=True)


with open('./1.txt', 'a') as f:
    for i in z:
        f.write('%s %s\n' %(i[0], i[1]))

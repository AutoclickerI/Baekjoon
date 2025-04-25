d=dict(zip(*[i.split()for i in open(0)][1:]))
print('bgaodo d'[all(d[d[i]]==i!=d[i]for i in d)::2])
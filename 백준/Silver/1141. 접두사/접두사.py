*l,={i[:-1]for i in open(0)}
for i in*l,:
    for j in*l,:
        if i.startswith(j) and i!=j:
            del l[l.index(j)]
print(len(l)-1)
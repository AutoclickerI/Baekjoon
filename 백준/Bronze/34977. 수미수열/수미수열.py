l=[*open(0)][1].split()
print('yneos'[all(l[:-i]!=l[i:]for i in range(1,len(l)))::2])
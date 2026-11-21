for i in open(0):
    *l,=map(int,i.split())
    l=[1]+l+[1]
    for j in range(2,len(l)):print(l[j-2]*l[j-1]*l[j],end=' ')
    print()
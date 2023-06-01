for i in[*map(int,open(0).read().split())][:-1]:
    k=sum(j+1for j in range(i)if i%(j+1)==0)
    if k>i*2:print(i,'ABUNDANT')
    if k==i*2:print(i,'PERFECT')
    if k<i*2:print(i,'DEFICIENT')
from itertools import*

for i in open(0):
    s,n=i.split()
    print(i+'=')
    n=int(n)-1
    for i,v in enumerate(permutations(sorted(s))):
        if i==n:break
    else:
        print('No permutation')
        continue
    print(*v,sep='')
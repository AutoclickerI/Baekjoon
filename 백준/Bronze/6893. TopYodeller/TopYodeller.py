n,m=map(int,input().split())
*l,=map(int,input().split())
*o,=map(sorted(l,key=lambda s:-s).index,l)
for _ in[0]*~-m:
    l=[i+j for i,j in zip(l,map(int,input().split()))]
    *o,=map(max,o,map(sorted(l,key=lambda s:-s).index,l))
for i in range(n):
    if l[i]==max(l):
        print(f'Yodeller {i+1} is the TopYodeller: score {l[i]}, worst rank {o[i]+1}')
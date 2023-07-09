input()
*l,=map(int,input().split())
d={j:i for i,j in enumerate(sorted(l))}
print(min(sum(d[i]+1!=d[j]for i,j in zip(l,l[1:]))+1,3))
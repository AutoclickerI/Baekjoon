from collections import*
n,k,*l=map(int,open(0).read().split())
print(k-len(c)if k>len(c:=Counter(l))else n-sum(i[1]for i in c.most_common(k)))
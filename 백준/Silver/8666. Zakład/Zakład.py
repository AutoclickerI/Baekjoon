from collections import*
n,k,*l=map(int,open(0).read().split())
print(max(k-len(c:=Counter(l)),n-sum(i for _,i in c.most_common(k))))
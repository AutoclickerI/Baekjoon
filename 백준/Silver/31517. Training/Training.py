(n,s),*L=[map(int,i.split())for i in open(0)]
for l,r in L:s+=l<=s<=r
print(s)
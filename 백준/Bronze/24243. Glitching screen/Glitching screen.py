a,*l=open(0)
h,_,n=map(int,a.split())
*s,c=map(''.join,zip(*[iter(l)]*h))
print('yneos'[sum(all(i in['.',j]for i,j in zip(c,t))for t in s)!=1::2])
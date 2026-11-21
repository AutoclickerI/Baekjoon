r=range
n,m=map(int,input().split())
for i in r(n):print(''.join('*.'[sum(-~j%k<1for k in r(1,j+2))>m]for j in r(i*n,i*n+n)) )
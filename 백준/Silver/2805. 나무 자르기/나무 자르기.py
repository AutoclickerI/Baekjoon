_,n,*l=map(int,open(s:=0).read().split())
e=1<<31
while~s+e:m=s+e>>1;exec('se'[sum(max(0,i-m)for i in l)<n]+'=m')
print(s)
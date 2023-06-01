import math
n,*l=map(int,open(0).read().split())
cnt1=[0]*30001
cnt2=[0]*30001
for i in l:cnt1[i]+=1
ans=sum(math.comb(i,3)for i in cnt1)
for i in l:
    cnt1[i]-=1
    for j in range(1,min(i,30001-i)):ans+=cnt1[i+j]*cnt2[i-j]+cnt1[i-j]*cnt2[i+j]
    cnt2[i]+=1
print(ans)
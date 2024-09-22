N=int(input())
s=input()
#%%
N=len(s)
import math
l=[]
cnt=0
f=0
ncnt=0
for idx,i in enumerate(s):
    if i=='>':
        if f:
            f=0
            cnt=0
            ncnt=0
        cnt+=1
        l+=-1,
    else:
        f=1
        if cnt>0:
            ncnt+=1
            l+=idx-ncnt*2+1,
        else:
            l+=-1,
        cnt-=1
#%%
ans=0
for idx,i in enumerate(l):
    if 0<=i:
        ans+=math.comb(N-idx+i-1,i)
print(ans%(10**9+7))
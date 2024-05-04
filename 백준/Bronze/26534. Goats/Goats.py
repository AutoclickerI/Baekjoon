f=lambda:map(int,input().split())

*A,=f()
cnt=[0]*7
for i in f():cnt[i]+=1

for i in range(2,7):
    cnt[i]+=cnt[i-1]
a,t=0,36
for n in A:
    a+=cnt[n-1]
    t-=cnt[n]-cnt[n-1]
a/=t
print('%.5f'%a)
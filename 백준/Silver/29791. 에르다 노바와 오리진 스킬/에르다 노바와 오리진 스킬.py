input()
cnt=[0,0]
tmp=-100
for i in sorted(map(int,input().split())):
    if i-tmp>99:
        cnt[0]+=1;tmp=i
tmp=-360
for i in sorted(map(int,input().split())):
    if i-tmp>359:
        cnt[1]+=1;tmp=i
print(*cnt)
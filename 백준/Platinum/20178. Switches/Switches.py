l=[]
n=int(input())
for i in range(n):
    l+=[int(input().replace(' ',''),2),1<<n-1-i],
idx=0
while idx<n:
    l.sort(reverse=True)
    for i in range(idx+1,n):
        if l[i][0]&(1<<n-1-idx):
            l[i][0]^=l[idx][0]
            l[i][1]^=l[idx][1]
        else:
            break
    idx+=1
while 0<idx:
    idx-=1
    for i in range(idx):
        if l[i][0]&(1<<n-1-idx):
            l[i][0]^=l[idx][0]
            l[i][1]^=l[idx][1]
if [i[0]for i in l]==[1<<n-1-i for i in range(n)]:
    for _,i in l:
        for i,v in enumerate(f'{i:b}'.zfill(n),1):
            if v=='1':print(i,end=' ')
        print()
else:
    print(-1)
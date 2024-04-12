_,M,*a=map(int,input().split())
s=input()[::-1]
f=0
for i in s:
    if f==0:
        if i not in'AEIOU':a+=i;f+=1
    elif f<3:
        if i=='A':a+=i;f+=1
    else:
        a+=i,
if len(a)<M:print('NO')
else:
    print('YES')
    print(*a[M-1::-1],sep='')
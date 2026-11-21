n,m=map(int,input().split())
d={}
l=[0]*n
for i in range(m):
    x,o,h,m=input().split();t=int(h)*60+int(m)
    if'A'==o[2]:d[x]=t
    else:l[int(x)-1]+=t-d[x]
for i in l:print(i//60,i%60)
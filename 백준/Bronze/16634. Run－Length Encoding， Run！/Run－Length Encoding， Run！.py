q,s=input().split()
if q=='E':
    l=[]
    p=c=[]
    for i in s:
        if i==p:
            c[-1]+=1
        else:
            c+=1,
            l+=i,
        p=i
    for i,j in zip(l,c):print(end=i+str(j))
else:
    for i,j in zip(*[iter(s)]*2):print(end=i*int(j))
        
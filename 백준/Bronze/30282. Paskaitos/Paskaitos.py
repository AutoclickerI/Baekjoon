t=[1440*[0]for _ in[0]*6]
a,tot='TAIP',0
for i in range(1,11):
    d,s1,e1,s2,e2=map(int,input().split())
    t1,t2=s1*60+e1,s2*60+e2
    tot+=t2-t1
    for j in range(t1,t2):
        if t[d][j]:
            a='NE';n=t[d][j],i
            break
        t[d][j]=i
    if a=='NE':
        break
print(a)
if a=='TAIP':
    print(*divmod(tot,60))
else:
    print(*n)
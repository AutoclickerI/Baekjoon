s,v1,v2=map(int,input().split())
t1=s//v1
t2=0
while-~t1:
    if t1*v1+t2*v2==s:exit(print(t1,t2))
    if t1*v1+t2*v2>s:
        t1-=1
    if t1*v1+t2*v2<s:
        t2+=1
print('Impossible')
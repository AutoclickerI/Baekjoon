p,q,r=map(int,input().split())
a=1
pos=p
while pos<r:
    a+=1
    pos+=p-q
print(a)
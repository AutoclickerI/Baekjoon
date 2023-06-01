e=int(input())-1
l=sorted(map(int,input().split()))
v=int(input())
s=0
a=0
while s<e:
    if l[s]+l[e]<v:
        s+=1
    else:
        a+=l[s]+l[e]==v
        e-=1
print(a)
N=int(input())

v=[0]*1000001
p=[0]*1000001

*l,=map(int,input().split())

for i in l:v[i]=1

for i in l:
    n=2*i
    while n<1000001:
        if v[n]:
            p[n]-=1
            p[i]+=1
        n+=i

for i in l:
    print(p[i])
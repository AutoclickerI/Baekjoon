N=int(input())
l=[0]+sorted(map(int,input().split()))
M=int(input())-sum(l)
c=1
v=l.pop()
while M<0:
    nv=l.pop()
    if -M<(v-nv)*c:
        M//=c
        v+=M
        M=0
        break
    else:
        M+=(v-nv)*c
        c+=1
    v=nv
print(v)
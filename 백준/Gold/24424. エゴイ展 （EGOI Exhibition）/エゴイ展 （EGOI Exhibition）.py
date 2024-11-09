import sys
input=sys.stdin.readline

N=int(input())
M=int(input())

l=[(0,0)]*2

for _ in[0]*N:
    a,v=map(int,input().split())
    new=sorted(l+[(v+p,a)for p,q in l if q!=a])
    l=[new[-1]]
    for i in new[-2::-1]:
        if l[0][1]!=i[1]:
            l+=i,
            break
print(max(l[0][0],l[1][0]))
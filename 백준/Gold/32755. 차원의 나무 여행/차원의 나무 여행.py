N=int(input())
l=[0]*-~N
for _ in[0]*~-N:
    s,e=map(int,input().split())
    l[s]+=1
    l[e]+=1
print(N-(max(l)==N-1))
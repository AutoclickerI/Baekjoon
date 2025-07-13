import sys
sys.setrecursionlimit(2*10**5)
input = sys.stdin.readline
parent = {}

def find(x):
    if x == parent[x]: 
        return x
    parent[x] = find(parent[x])
    return parent[x]

def union(x,y):
    x = find(x)
    y = find(y)
    if y < x:
        parent[x] = y

    else:
        parent[y] = x

N,*l=map(int,open(0))
x=0
p=l[0]-1
x=0
idx=0
v=N

for y in l:
    if y<=p:
        x+=1
    if(y-1,x)in parent:
        parent[y,x]=find(parent[y-1,x])
        v-=1
        if(y,x-1)in parent:
            if find(parent[y,x])!=find(parent[y,x-1]):
                union(parent[y,x],parent[y,x-1])
                v-=1
    elif(y,x-1)in parent:
        parent[y,x]=find(parent[y,x-1])
        v-=1
    else:
        idx+=1
        parent[y,x]=idx
        parent[idx]=idx
    p=y

print(v)
print(N)
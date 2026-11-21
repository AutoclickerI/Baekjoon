import sys
input=sys.stdin.readline
N,Q=map(int,input().split())
color=[0]*-~N
tree=4*-~N*[0]
def update(start,end,index,area_start,area_end,c):
    if tree[index]or end<area_start or start>area_end:
        return
    tree[index]=area_start<=start<=end<=area_end
    if start-end:
        mid=(start+end)//2
        update(start,mid,2*index,area_start,area_end,c)
        update(mid+1,end,2*index+1,area_start,area_end,c)
    else:
        color[start]=c
for _ in range(Q):
    s,e,t=map(int,input().split())
    update(0,N,1,s,e,t)
print(*color[1:])
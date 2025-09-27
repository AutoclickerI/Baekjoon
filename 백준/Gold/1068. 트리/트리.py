N=int(input())
d={}
l=input().split()
for i in range(N):
    d[int(l[i])]=d.get(int(l[i]),[])+[i]
v=int(input())
if v in d:del d[v]
a=0
for i in*d,:
    if d[i]==[v]:del d[i]
def traverse(n):
    global a
    if n in d:
        for e in d[n]:
            traverse(e)
    else:
        a+=n not in[v,-1]
traverse(-1)
print(a)
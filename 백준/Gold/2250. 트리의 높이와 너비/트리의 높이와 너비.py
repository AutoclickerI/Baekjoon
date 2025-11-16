[N],*l=[map(int,i.split())for i in open(0)]
d={}
v={*range(1,N+1)}
for r,*s in l:d[r]=s;v-={*s}
[r]=v
cnt=0
v=[]
def traverse(n,depth):
    global cnt
    if n<1:
        return
    l,r=d[n]
    if len(v)<=depth:
        v.append([])
    traverse(l,depth+1)
    cnt+=1
    v[depth]+=cnt,
    traverse(r,depth+1)
traverse(r,0)
v=[1+i[-1]-i[0]for i in v]
mv=max(v)
print(v.index(mv)+1,mv)
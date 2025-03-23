*l,_=map(int,input().split())

d={(0,0):0}

def cost(f,t):
    if f==0:
        return 2
    return[1,3,4,3][abs(f-t)]

for i in l:
    t={}
    for x,y in d:
        c=d[x,y]
        opt1=*sorted([i,y]),
        t[opt1]=min(t.get(opt1,1e9),d[x,y]+cost(x,i))
        opt2=*sorted([i,x]),
        t[opt2]=min(t.get(opt2,1e9),d[x,y]+cost(y,i))
    d=t

print(min(d.values()))
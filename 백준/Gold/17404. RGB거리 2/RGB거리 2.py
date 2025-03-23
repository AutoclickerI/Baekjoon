l=[[*map(int,i.split())]for i in open(0)][1:]

tmp=[*l[0]]

a=[]

for p in 0,1,2:
    l[0]=[1e9]*3
    l[0][p]=tmp[p]
    d=[0]*3
    for x,y,z in l:
        d=[min(d[1:])+x,min(d[0],d[2])+y,min(d[:2])+z]
    del d[p]
    a+=d
    l[0]=[*tmp]

print(min(a))
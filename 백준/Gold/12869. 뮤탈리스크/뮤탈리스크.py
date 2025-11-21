l=*sorted((*map(int,[*open(0)][1].split()),0,0))[-3:],
v={l:0}
l=[(0,l)]
for c,i in l:
    for d in(9,3,1),(9,1,3),(3,9,1),(3,1,9),(1,9,3),(1,3,9):
        n=*sorted(map(max,map(int.__sub__,i,d),(0,0,0))),
        if n not in v:
            v[n]=c+1
            l+=(c+1,n),
print(v[0,0,0])
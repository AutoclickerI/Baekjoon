p=[[1]]
for _ in[0]*99:
    p+=[1]+[*map(sum,zip(p[-1],p[-1][1:]))]+[1],

R,C,W=map(int,input().split())
v=0
for w in range(W):
    for x in range(C-1,C+w):
        v+=p[R-1+w][x]
print(v)
curve=[(0,0),(1,0)]
gen=[curve]

for _ in[0]*10:
    rot=[(-y,x)for x,y in curve][::-1]
    dx=rot[0][0]-curve[-1][0]
    dy=rot[0][1]-curve[-1][1]
    curve=curve+[(x-dx,y-dy)for x,y in rot][1:]
    gen+=curve,

se=set()

for i in[*open(0)][1:]:
    x,y,d,g=map(int,i.split())
    d^=d%2*2
    curve=gen[g]
    for _ in[0]*d:
        curve=[(-y,x)for x,y in curve]
    dx=x-curve[0][0]
    dy=y-curve[0][1]
    se|={(x+dx,y+dy)for x,y in curve}

v=0
for y in range(100):
    for x in range(100):
        v+={(x,y),(x+1,y),(x,y+1),(x+1,y+1)}<=se
print(v)
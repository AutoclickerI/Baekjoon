l=[]
for i in[*open(0)][1:]:_,s,e=map(int,i.split());l+=(s,1),(e,-1)
v=mv=0
for _,d in sorted(l):
    v+=d;mv=max(mv,v)
print(mv)
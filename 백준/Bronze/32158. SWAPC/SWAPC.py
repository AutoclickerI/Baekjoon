_,s=open(0)
c=min(map(s.count,'PC'))
for i in'P_','CP','_C':s=s.replace(*i,c)
print(s)
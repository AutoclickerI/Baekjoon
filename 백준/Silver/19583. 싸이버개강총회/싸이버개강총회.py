[S,E,Q],*l=[i.split()for i in open(0)]
s,*e=[],
for t,c in l:s+=[c]*(t<=S);e+=[c]*(E<=t<=Q)
print(len({*s}&{*e}))
d={}
for i in[*open(0)][1:]:
    _,s,_,*l=i.split()
    for i in l:d[s,i]=d.get((s,i),0)+1
s,i=max(d,key=d.get)
print(f'Your professor should host office hours {s} @ {int(i):02}:00')
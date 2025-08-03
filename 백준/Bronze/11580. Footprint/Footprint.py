x=y=0
s={(0,0)}
for c in[*open(0)][1]:x+=(c=='E')-(c=='W');y+=(c=='S')-(c=='N');s|={(x,y)}
print(len(s))
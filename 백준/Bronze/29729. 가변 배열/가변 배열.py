S,*l=open(o:=0)
S=int(S[:2])
for i in l:o+=2*int(i)-1;S*=1+(o>S)
print(S)
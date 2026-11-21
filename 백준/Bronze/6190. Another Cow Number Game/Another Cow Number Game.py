s,*l=int(input()),
while s>1:l+=(s:=3*s+1if s%2else s//2),
print(len(l))
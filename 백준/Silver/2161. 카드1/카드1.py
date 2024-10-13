*l,=range(int(input()))
r=[]
while len(l)>1:r+=l[0]+1,;l=*l[2:],l[1]
print(*r,l[0]+1)
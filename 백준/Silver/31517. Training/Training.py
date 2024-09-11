(n,s),*L=map(str.split,open(0))
s=int(s)
for l,r in L:s+=int(l)<=s<=int(r)
print(s)
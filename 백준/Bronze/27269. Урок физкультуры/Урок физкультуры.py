b,g=l=[[],[]]
for i in[*open(0)][1:]:a,h=map(int,i.split());l[a]+=h,
b.sort()
g.sort()
s=g+b
print(max(abs(i-j)for i,j in zip(s,s[1:])))
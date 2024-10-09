(n,m),*s=[[*map(int,i.split())]for i in open(0)]
for i,j in zip(s,s[1:]):
 if i[1]!=j[1]and(i[1]^(i[0]<j[0])):i[0],j[0]=j[0],i[0]
print(sum(i[1]^(i[0]>m)for i in s))
a,l={*map(chr,range(104,113))}|{'u'},[0,0,0]
for i in input():l[2]+=i<']';l[i.lower()in a]+=i!=' '
while l[2]:l[2]-=1;l[l[1]<l[0]]+=1
print(*l[:2])
a=[0]*9999
for s in[*open(0)][1:]:
 i,j,k=map(int,s.split())
 while i<j:a[i]+=k;i+=1
print(max(a))
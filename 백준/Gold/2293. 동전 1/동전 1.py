n,k,*c=map(int,open(0).read().split())
t=[1]+[0]*k
for i in c:
 for j in range(k-i+1):t[j+i]+=t[j]
print(t[k])
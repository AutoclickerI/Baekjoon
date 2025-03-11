a=open(0).read().split()
n,m,k,*l=map(int,a[:3])
d=a[4:3+2*m:2]
for i in range(m,n):
 if~-((q:=a[2*i+4])in d)*k:l+=a[2*i+3],;d+=q,;k-=1
print(len(l),*l)
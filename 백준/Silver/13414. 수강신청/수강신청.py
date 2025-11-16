K,L,*l=open(0).read().split()
s={}
for i in l[::-1]:s[i]=1
print(*[*s][:~int(K):-1])
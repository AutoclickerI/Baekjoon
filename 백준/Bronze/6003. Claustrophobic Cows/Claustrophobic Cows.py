_,*l=[eval(i.replace(' ','+1j*'))for i in open(0)]
m=1e9
for i in range(len(l)):
    for j in range(i+1,len(l)):
        v=abs(l[i]-l[j])
        if v<m:m=v;a=i+1,j+1
print(*a)
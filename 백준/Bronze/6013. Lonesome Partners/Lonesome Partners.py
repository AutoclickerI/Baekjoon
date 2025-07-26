N,*l=[eval(i.replace(' ','j+'))for i in open(0)]
print(*min((-abs(l[i]-l[j]),i+1,j+1)for i in range(N)for j in range(N))[1:])
n,*l=map(int,open(0).read().split())
print(sum(sum(z)/len(z)in z for i in range(n)for j in range(n+1)if(z:=l[i:j])))
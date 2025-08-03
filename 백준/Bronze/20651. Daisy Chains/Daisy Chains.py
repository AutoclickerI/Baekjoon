n,*l=map(int,open(0).read().split())
print(sum(sum(z)/len(z)in z for i in range(n*-~n)if(z:=l[i%n:i//n])))
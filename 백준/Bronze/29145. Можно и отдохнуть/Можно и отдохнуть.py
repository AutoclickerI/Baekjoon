(_,k),*l=[map(int,i.split())for i in open(0)]
print(sum(c*((z:=k-a)%b==0<=z)for a,b,c in l))
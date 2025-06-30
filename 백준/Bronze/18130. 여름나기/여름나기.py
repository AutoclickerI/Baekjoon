(_,q),*l=[map(int,i.split())for i in open(0)]
v=0
print(*min((i-(x:=q//-j)*~x//2*k,v:=v+1)for i,j,k in l)[::-1])
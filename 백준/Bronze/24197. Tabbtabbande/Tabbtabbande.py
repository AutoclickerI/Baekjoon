N,_,*l=map(int,open(0).read().split())
s=1
print(sum(min((i-s)%N,(s-(s:=i))%N)for i in l))
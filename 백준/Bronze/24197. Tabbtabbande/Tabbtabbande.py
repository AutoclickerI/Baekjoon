N,_,*l=map(int,open(a:=0).read().split())
s=1
for i in l:a+=min((i-s)%N,(s-i)%N);s=i
print(a)
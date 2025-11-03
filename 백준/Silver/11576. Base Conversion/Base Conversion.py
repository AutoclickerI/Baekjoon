A,B,_,*l=map(int,open(n:=0).read().split())
for i in l:n*=A;n+=i
a=[]
while n:a=n%B,*a;n//=B
print(*a)
_,i,*l=map(int,open(0))
print(sum(min(a:=abs(i-(i:=j)),360-a)for j in l))
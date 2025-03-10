_,*l=[[*map(int,i.split())]for i in open(0)]
i=0
while i:=i+1:all(j<=i%(j+k)for j,k in l)and exit(print(i))
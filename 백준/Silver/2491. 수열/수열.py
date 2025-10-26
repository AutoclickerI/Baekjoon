p=x=y=z=0
for i in[*open(0)][1].split():i=int(i);z=max(x:=1+(p<=i)*x,y:=1+(i<=p)*y,z);p=i
print(z)
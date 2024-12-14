n,s=open(0)
b=p=0
for i in range(int(n)):p+=(i-~b)*(t:=s[i]<'X');b=[0,b+1][t]
print(p)
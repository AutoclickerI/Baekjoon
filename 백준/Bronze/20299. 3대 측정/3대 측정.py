p,q,r,*s=map(int,open(0).read().split())
c=[]
for i in range(p):
 if sum(P:=s[3*i:3*i+3])>=q and min(P)>=r:c+=P
print(len(c)//3,*c)
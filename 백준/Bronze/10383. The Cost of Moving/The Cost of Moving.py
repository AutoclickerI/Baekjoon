*x,_=open(0).read().split()
s=1
while x:
 n=int(x.pop(0))
 i=x[:n];x=x[n:]
 R=range(n)
 l=sorted(zip(i,R));print(f'Site {s}:',sum(abs(l[i][1]-i)for i in R));s+=1
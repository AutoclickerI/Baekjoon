*x,_=open(s:=0).read().split()
while x:s+=1;R=range(n:=int(x.pop(0)));i=x[:n];x=x[n:];print(f'Site {s}:',sum(abs(i-j)for(_,i),j in zip(sorted(zip(i,R)),R)))
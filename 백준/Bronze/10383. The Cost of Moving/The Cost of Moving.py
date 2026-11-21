*x,_=open(s:=0).read().split()
while x:s+=1;n=int(x.pop(0));i=x[:n];x=x[n:];print(f'Site {s}:',sum(abs(j-sorted(i).index(i[j]))for j in range(n)))
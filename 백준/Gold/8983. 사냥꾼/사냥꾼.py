from bisect import*
a=0
[M,N,L],P,*l=[map(int,i.split())for i in open(0)]
for X,Y in l:Y-=L;a+=Y<=0!=bisect_left(P:=sorted(P),X+Y)-bisect(P,X-Y)
print(a)
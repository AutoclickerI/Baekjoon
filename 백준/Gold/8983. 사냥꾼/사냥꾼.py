from bisect import*
[M,N,L],P,*l=[map(int,i.split())for i in open(0)]
P=sorted(P)
print(sum(Y-L<=0!=bisect_left(P,X+Y-L)-bisect(P,X-Y+L)for X,Y in l))
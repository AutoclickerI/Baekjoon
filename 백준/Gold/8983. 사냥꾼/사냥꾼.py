from bisect import*
a=0
[M,N,L],P,*l=[map(int,i.split())for i in open(0)]
P=sorted(P)
for X,Y in l:a+=Y-L<=0!=bisect_left(P,X+Y-L)-bisect(P,X-Y+L)
print(a)
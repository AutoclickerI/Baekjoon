from bisect import*
(n,m),[k,*t],x=[map(int,i.split())for i in open(0)]
l=k,*[k:=max(k,i)for i in t]
print(*map(bisect_left,[l]*m,x))
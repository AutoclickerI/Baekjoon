_,[p,q],*a=[map(int,i.split())for i in open(0)]
m=0
for t,d in a:m=max(m,(d-q)//(t-p));p,q=t,d
print(m)
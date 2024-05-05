_,p,q=open(0)
print(*sorted({*p.split()}&{*q.split()},key=int))
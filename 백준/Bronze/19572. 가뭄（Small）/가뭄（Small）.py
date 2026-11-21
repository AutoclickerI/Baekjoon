p,q,r=map(int,input().split())
s=(p+q+r)/2
l=1,s-r,s-q,s-p
print(*[[-1],l][min(l)>0])
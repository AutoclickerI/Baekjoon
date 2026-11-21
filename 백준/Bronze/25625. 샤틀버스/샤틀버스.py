p,q=map(int,input().split())
q+=5*p
while p<q:q-=2*p
print(q+2*p*(q<0))
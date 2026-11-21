input()
*l,=map(int,input().split())
a=0
while l[1:]:p,q,*l=l;l+=p+q,;a+=p*q
print(a)
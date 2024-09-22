c=0
N=int(input())
while 1:
 r,q=divmod(N,3);c+=1
 if r<1or (r==1>q):break
 N=r+(0<q)
print(c)
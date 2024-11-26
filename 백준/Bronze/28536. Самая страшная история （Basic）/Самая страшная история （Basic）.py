from bisect import bisect_left
n,_,*z=open(0).read().split()
l=[0]
for i in z[:int(n)]:l+=len(i)+l[-1],
for v in z[int(n):]:
    v=int(v)
    print(i:=bisect_left(l,v),v-l[i-1])
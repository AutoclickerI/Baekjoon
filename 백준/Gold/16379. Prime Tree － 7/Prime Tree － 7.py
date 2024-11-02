maxlen=10**5+1
fac=[[]for _ in[0]*maxlen]
for i in range(2,maxlen):
    if len(fac[i])<1:
        fac[i]+=i,
        for j in range(2*i,maxlen,i):
            fac[j]+=i,
primes=[i for i in range(2,maxlen)if fac[i][0]==i]

from bisect import bisect_right
for T in[0]*int(input()):
    n=int(input())
    l=[[]for _ in[0]*-~n]
    v=[-1]*-~n
    for _ in[0]*~-n:s,e=map(int,input().split());l[s]+=e,;l[e]+=s,
    idx_lst=sorted(range(1,n+1),key=lambda i:len(l[i]))
    p_c=primes[:bisect_right(primes,n)]+[1]
    bad=[i for i in range(2,n+1)if fac[i][0]!=i]
    bad.sort(key=lambda i:len(fac[i]))
    while idx_lst and p_c:
        v[idx_lst.pop()]=p_c.pop()
    while idx_lst:
        node=idx_lst.pop()
        lst=[i for i in l[node]if v[i]<0]
        i=-1
        while bad[i]in lst:i-=1
        x=bad.pop(i)
        v[node]=x
    print(*v[1:])
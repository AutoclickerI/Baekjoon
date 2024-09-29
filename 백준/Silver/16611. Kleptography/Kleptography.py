p,q,r=open(0)
n,m=map(int,p.split())
for i in range(m-n,0,-1):q=chr((ord(r[i+n-1])-ord(q[n-1]))%26+97)+q
print(q)
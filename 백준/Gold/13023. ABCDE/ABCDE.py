R=lambda:map(int,input().split())
n,m=R()
d=[]
f=lambda v,z={-1}:4<len(z)or+any(f(w,z|{v})for w in d[v]if{w}-z)
exec('d+=[],;'*n+'a,b=R();d[a]+=b,;d[b]+=a,;'*m)
print(max(map(f,range(n))))
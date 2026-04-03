s=input()

n=1
v='1'
while len(v)-len(s):
    n+=1
    v+=str(n)
v=[0]*-~n
r=[]
def backtrack(i):
    if i==len(s):
        exit(print(*r))
    if i+1<len(s):
        nn=int(s[i:i+2])
        if nn<=n and v[nn]<1:
            v[nn]=1
            r.append(nn)
            backtrack(i+2)
            r.pop()
            v[nn]=0
    nn=int(s[i])
    if nn<=n and v[nn]<1:
        v[nn]=1
        r.append(nn)
        backtrack(i+1)
        r.pop()
        v[nn]=0
backtrack(0)
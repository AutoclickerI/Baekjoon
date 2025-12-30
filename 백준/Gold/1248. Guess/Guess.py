v=N=int(input())
s=input()
l=[]
while v:
    l+=s[:v],
    s=s[v:]
    v-=1
v=[0]*N

def sign(v):
    if 0<v:
        return'+'
    if v<0:
        return'-'
    return'0'

def backtrack(n):
    if n<0:
        raise
    if l[n][0]=='+':
        *p,=range(1,11)
    if l[n][0]=='0':
        p=[0]
    if l[n][0]=='-':
        *p,=range(-10,0)
    for i in p:
        v[n]=i
        f=1
        for e in range(1,N-n):
            if l[n][e]!=sign(sum(v[n:n+e+1])):
                f=0
        if f:
            backtrack(n-1)
try:
    backtrack(N-1)
except:
    print(*v)
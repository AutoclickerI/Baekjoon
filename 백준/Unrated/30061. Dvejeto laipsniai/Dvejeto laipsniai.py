N=int(input())
D=input()
c=[0]*10
for i in D:c[int(i)]+=1
mv=-1
r=-1
pow10=tuple(10**i for i in range(20))
def backtrack(n,v):
    global mv,r
    nn=n+1
    if n==N:
        cc=0
        vv=v
        while vv%2<1:
            cc+=1
            vv//=2
        if mv<cc:
            mv=cc
            r=v
    for i in range(10):
        if c[i]:
            v+=i*pow10[n]
            c[i]-=1
            if v&(1<<nn)-1<1:
                backtrack(nn,v)
            elif mv<n:
                mv=n
                r=v
            c[i]+=1
            v-=i*pow10[n]
backtrack(0,0)
if sorted(str(r))!=sorted(D):
    for i in str(r):
        c[int(i)]-=1
    s=''
    for i in range(9,0,-1):
        s+=str(i)*c[i]
    r=s+str(r)
print(r)
print(2**mv)
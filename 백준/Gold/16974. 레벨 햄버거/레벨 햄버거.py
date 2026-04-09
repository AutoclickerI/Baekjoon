#(B,P)
H=[(0,1)]
b=0
p=1
for _ in[0]*50:
    b,p=b*2+2,p*2+1
    H+=(b,p),

def recur(N,X):
    if X==0:
        return 0
    if X==sum(H[N]):
        return H[N][1]
    if sum(H[N-1])<X:
        r=H[N-1][1]
        X-=sum(H[N-1])+1
        if X<1:
            return r
        else:
            return r+1+recur(N,X)
    else:
        return recur(N-1,X-1)

print(recur(*map(int,input().split())))
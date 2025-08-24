mod=998244353
# even numbers from -M to M
def geteven(M):
    return M//2*2+1
def getquarter(M):
    return M//4*2+1
for i in[*open(0)][1:]:
    A,B,M=map(int,i.split())
    if abs(A)==1 and B==0:
        print((2*M+1)**2%mod)
    elif A==0 and abs(B)==1:
        print((2*M+1)*geteven(M)%mod)
    elif A==0 and B==0:
        print(M%mod)
    else:
        if abs(A)==abs(B):
            print(getquarter(M)%mod)
        elif A==0:
            print(geteven(M)%mod)
        elif B==0:
            print((2*M+1)%mod)
        else:
            print(1)
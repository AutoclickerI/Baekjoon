import sys
input=sys.stdin.readline

mod=10**9+7

def cmul(a,b,c,d):
    return(a*c-b*d)%mod,(a*d+b*c)%mod

def csub(a,b,c,d):
    return(a-c)%mod,(b-d)%mod

def cinv(a,b):
    t=pow(a*a+b*b,-1,mod)
    return a*t,-b*t

def cpow(a,b,k):
    res_r,res_i=1,0
    base_r, base_i = a, b

    while k > 0:
        if k & 1:
            res_r, res_i = cmul(res_r, res_i, base_r, base_i)
        base_r, base_i = cmul(base_r, base_i, base_r, base_i)
        k >>= 1

    return res_r, res_i

for Q in range(int(input())):
    i,j,k=map(int,input().split())
    a,b=cpow(1,-2,k)
    print(cmul(*csub(*cpow(a,b,j+1),*cpow(a,b,i)),*cinv(a-1,b))[0])
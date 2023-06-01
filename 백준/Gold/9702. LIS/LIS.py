from bisect import*
def LIS(n,l):
    d=[m:=0]
    c=[-2e+9]
    ans=0
    for i in range(n):
     if c[-1]<l[i]:d+=[m:=len(c)];c+=[l[i]]
     else:d+=[L:=bisect_left(c,l[i])];c[L]=l[i]
     ans+=m
    return ans
for i in range(int(input())):
    n=int(input())
    l=[int(input())for _ in[0]*n]
    num=0
    for j in range(n):
        num+=LIS(n-j,l[j:])
    print(f'Case #{i+1}: {num}')
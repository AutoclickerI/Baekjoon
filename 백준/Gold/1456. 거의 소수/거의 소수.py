*p,=range(10**7+1)
p[1]=0
for i in range(2,10**7+1):
    if p[i]:
        p[2*i::i]=[0]*len(range(2*i,10**7+1,i))
p=[i for i in p if i]

def c(n):
    r=0
    for i in p:
        j=i*i
        while j<=n:
            r+=1
            j*=i
    return r
A,B=map(int,input().split())
print(c(B)-c(A-1))
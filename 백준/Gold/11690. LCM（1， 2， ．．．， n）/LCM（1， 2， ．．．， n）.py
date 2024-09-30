N=int(input())
l=bytearray(N//8+2)
def get(n):
    return l[n//8]&1<<n%8
def set(n):
    l[n//8]|=1<<n%8
a=1
for i in range(2,N+1):
    if get(i):
        continue
    else:
        for j in range(i*2,N+1,i):set(j)
        j=i
        while j*i<N+1:
            j*=i
        a=a*j%2**32
print(a)
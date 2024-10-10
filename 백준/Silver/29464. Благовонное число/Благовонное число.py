n=int(input())
s=f=0
while 9*10**s<n:
    n-=9*10**s
    s+=f
    f^=1
a=str(n+10**s-1)
print(a[:len(a)-1+f]+a[::-1])
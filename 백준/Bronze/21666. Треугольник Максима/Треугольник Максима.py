from decimal import*
getcontext().prec=99
m=30
M=4000
n=int(input())
prev=Decimal(input())
for _ in[0]*~-n:
    p,q=input().split()
    p=Decimal(p)
    if q=='closer':
        if prev<p:
            m=max(m,(p+prev)/2)
        if prev>p:
            M=min(M,(p+prev)/2)
    else:
        if prev>p:
            m=max(m,(p+prev)/2)
        if prev<p:
            M=min(M,(p+prev)/2)
    prev=p
print(f'{m:.99f} {M:.99f}')
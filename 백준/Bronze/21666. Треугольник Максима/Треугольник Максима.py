m=30
M=4000
n=int(input())
prev=eval(input())
for _ in[0]*~-n:
    p,q=input().split()
    p=eval(p)
    if prev==p:0
    elif(q=='closer')^(prev>p):m=max(m,(p+prev)/2)
    else:M=min(M,(p+prev)/2)
    prev=p
print(m,M)
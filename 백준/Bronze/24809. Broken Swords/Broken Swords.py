p=q=0
for _ in[0]*int(input()):
    t,b,l,r=map(int,input())
    p+=2-t-b
    q+=2-l-r
print(n:=min(p//2,q//2),p-2*n,q-2*n)
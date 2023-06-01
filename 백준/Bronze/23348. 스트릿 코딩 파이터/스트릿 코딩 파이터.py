p,q,r=map(int,input().split())
a=[]
for i in[0]*int(input()):
    ans=0
    for j in[0]*3:
        P,Q,R=map(int,input().split())
        ans+=p*P+q*Q+r*R
    a+=[ans]
print(max(a))
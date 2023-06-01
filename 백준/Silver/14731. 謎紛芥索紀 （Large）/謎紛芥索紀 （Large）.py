a=0
for _ in[0]*int(input()):
    p,q=map(int,input().split())
    a+=p*q*pow(2,q-1,10**9+7)
print(a%(10**9+7))
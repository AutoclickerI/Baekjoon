p,q=map(int,input().split())
s=0
for i in range(p):
    s*=10**len(str(i+1))
    s+=i+1
    s%=q
print(s)
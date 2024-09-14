p,q=sorted(map(int,input().split()))
a=0
while p:a+=q//p;p,q=q%p,p
print(a)
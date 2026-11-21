n,b=map(int,input().split())
a=q=0
for i in map(int,input().split()):q+=i;a+=q;q-=min(b,q)
print(a+q)
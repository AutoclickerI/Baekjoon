_,a,b=map(int,input().split())
a,b=sorted((a,b))
a-=1
b-=1
c=1
while a+1!=b or a%2:
    c+=1
    a//=2
    b//=2
print(c)
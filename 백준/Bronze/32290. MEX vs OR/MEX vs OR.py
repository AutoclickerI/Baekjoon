l,r,x=map(int,input().split())
s={i|x for i in range(l,r+1)}
a=0
while a in s:a+=1
print(a)
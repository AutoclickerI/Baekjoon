N,_=map(int,input().split())
*l,=map(int,input().split())
s=1
a=0
for i in l:
    a+=min((i-s)%N,(s-i)%N)
    s=i
print(a)
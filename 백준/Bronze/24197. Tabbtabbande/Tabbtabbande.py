N,_=map(int,input().split())
l=[i-1 for i in map(int,input().split())]
s=0
a=0
for i in l:
    a+=min((i-s)%N,(s-i)%N)
    s=i
print(a)
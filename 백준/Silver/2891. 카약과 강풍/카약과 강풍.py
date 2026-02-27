N,S,R=map(int,input().split())
b={*map(int,input().split())}
s={*map(int,input().split())}
j=s&b
b-=j
s-=j
for i in sorted(s):
    if i-1 in b:
        b.remove(i-1)
    elif i+1 in b:
        b.remove(i+1)
print(len(b))
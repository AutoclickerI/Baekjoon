n=int(input())
l=[input().split()for _ in[0]*n]
while len(l)>1:
    a,b=l.pop(0)
    exec(int(b)%len(l)*"l+=l.pop(0),;")
    l.pop()
print(l[0][0])
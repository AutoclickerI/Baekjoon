N,M=map(int,input().split())
t={}
m={}
for _ in[0]*N:
    s=input()
    l=[input()for _ in[0]*int(input())]
    t[s]=sorted(l)
    for i in l:m[i]=s
for _ in[0]*M:
    s=input()
    if'0'<input():
        print(m[s])
    else:print(*t[s])
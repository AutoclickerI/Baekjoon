m=0
for _ in[s:=0]*int(input()):
    s+=int(input())
    m=min(m,s)
print(-m)
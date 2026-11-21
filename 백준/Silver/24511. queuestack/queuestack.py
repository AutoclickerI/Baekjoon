f=lambda:map(int,input().split())
f()
l=[j for i,j in zip(f(),f())if~-i][::-1]
n,=f()
l+=f()
print(*l[:n])
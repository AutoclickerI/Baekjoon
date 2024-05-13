f=lambda:[*map(int,input().split())]
f()
print(sum(a:=f()),sum(s-s*t for s,t in zip(a,f())))
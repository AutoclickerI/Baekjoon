f=lambda:[*map(int,input().split())]
while any(l:=f()):w=f();print(*map(''.join(str(i*j)for i in f()for j in w).count,'0123456789'))
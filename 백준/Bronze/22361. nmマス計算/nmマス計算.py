f=lambda:[*map(int,input().split())]
while(l:=f())[0]:w=f();print(*map(''.join(str(i*j)for i in f()for j in w).count,'0123456789'))
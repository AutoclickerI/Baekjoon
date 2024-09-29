f=lambda:[*map(int,input().split())]
while sum(s:=f()):A,C=s;a=c=0;[a:=a-c+max(c,c:=A-i)for i in f()];print(a)
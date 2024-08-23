f=lambda:map(int,input().split())
f()
s=sorted(f())
print(m:=min(a:=[j-i for i,j in zip(s,s[1:])]),a.count(m))
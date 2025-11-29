n,*l=map(int,[*open(0)][f:=1].split())
for i in l:n=(n+1//i)*i%(10**9+7)+f*(n<2<=i);f=0
print(n)
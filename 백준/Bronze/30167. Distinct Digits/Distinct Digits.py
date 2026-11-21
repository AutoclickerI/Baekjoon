p,q=map(int,input().split())
print(~min(~i*(len(s:=str(i))==len({*s}))for i in range(p,q+1)))
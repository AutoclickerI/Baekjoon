a,b=input().split()
f=lambda x:['%s','(%s)'][int(x)<0]%x
T={eval(t:=f(a)+i+f(b)):t for i in'+-*'}
print(['NIE',T[m:=max(T)]+'='+f(m)][len(T)>2])
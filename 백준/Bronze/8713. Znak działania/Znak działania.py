a,b=input().split()
f=lambda x:[f'{x}',f'({x})'][int(x)<0]
T={eval(t:=f(a)+i+f(b)):t for i in'+-*'}
print(['NIE',T[m:=max(T)]+'='+f(m)][len(T)>2])
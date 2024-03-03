def f(b):d=0;print(len([d:=x for x in b if x>d]))
_,*l=map(int,open(0))
f(l);f(l[::-1])
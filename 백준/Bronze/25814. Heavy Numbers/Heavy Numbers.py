p,q=input().split()
f=lambda s:len(s)*eval('+'.join(s))
print('021'[(f(p)<f(q))-(f(p)>f(q))])
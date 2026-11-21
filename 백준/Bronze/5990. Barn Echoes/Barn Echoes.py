p,q=open(0)
f=lambda p,q:max(i for i in range(len(p))if q[:-1].endswith(p[:i]))
print(max(f(p,q),f(q,p)))
_,*s=open(0)
t=sorted(s)
print(['NEITHER','INCREASING','DECREASING'][(s<t[::-1])-(t<s)])
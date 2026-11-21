_,*a=open(0)
print(+all(any(t[:i]in s[~i:]or s[:i]in t[~i:]for i in range(1,111))for s,t in zip(a,a[1:])))
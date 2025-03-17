n,s=open(0)
n=int(n)
print('NYoe s'[any(s[:-1]==n//i*s[:i]for i in range(1,n))::2])
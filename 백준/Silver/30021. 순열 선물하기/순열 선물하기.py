n=int(input())
f=n!=2
print('NYOE S'[f::2],*(*'132'*f,*range(4,n+1))[:n])
f=lambda:map(int,input().split()[1:])
exec('*a,=f();print(min(abs(x-y)for x in f()for y in a));'*int(input()))
n,a=open(0)
exec(f'a=[{a}]'+';a=[j-i for i,j in zip(a,a[1:])]'*int(n[2:]))
print(*a,sep=',')
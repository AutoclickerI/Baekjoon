f=lambda:map(int,input().split())
for j in range(*f()):
    N,L,H=f();*x,=f()
    u=0
    for i in range(L,H+1):
        if all(1-(i%p>0<p%i)for p in x):u=1;break
    print(f'Case #{j+1}:',['NO',i][u])
f=lambda:map(int,input().split())
for i in range(*f()):n,m,l=f();x=max([l]+[m-i for i in f()if~i]);print(f'The scoreboard has been frozen with {x} minute'+'s'*(x>1),'remaining.')
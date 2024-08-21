I=input
f=lambda:sorted(map(int,I().split()))
for i in range(f()[0]):I();print(f'Case #{i+1}:',sum(x*y for x,y in zip(f(),f()[::-1])))
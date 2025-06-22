f=lambda:map(int,input().split())
for T in range(*f()):
    C,I=*f(),*f();*l,=f()
    for i in range(I):
        for j in range(i+1,I):l[i]+l[j]==C!=print(f'Case #{T+1}:',i+1,j+1)
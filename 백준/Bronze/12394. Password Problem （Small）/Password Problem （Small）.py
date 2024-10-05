f=lambda:map(eval,input().split())
for T in range(*f()):
 A,B=f();l=1,*f();m=B+2;c=1
 for n in range(A+1):c*=l[n];m=min(m,2*B+c*~B+A-2*n+2)
 print(f'Case #{T+1}:',m)
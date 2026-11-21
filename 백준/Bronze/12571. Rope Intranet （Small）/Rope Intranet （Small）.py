I=lambda:map(int,input().split())
for i in range(*I()):
 [n]=I();a,b=I()
 if n>1:c,d=I()
 print(f'Case #{i+1}:',+(n>1>(a-c)*(b-d)))
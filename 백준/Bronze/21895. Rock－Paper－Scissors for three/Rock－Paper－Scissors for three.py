a,b,c=open(0)
f=lambda i:1<<'RSP'.find(i)
for i,j in zip(b[:-1],c):print(end=' PRRSPS'[f(i)|f(j)])
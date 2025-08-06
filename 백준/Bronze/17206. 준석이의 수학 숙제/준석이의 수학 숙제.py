f=lambda i:i*~i//-2
for n in[*open(0)][1].split():n=int(n);print(f(n//3)*3+f(n//7)*7-f(n//21)*21)
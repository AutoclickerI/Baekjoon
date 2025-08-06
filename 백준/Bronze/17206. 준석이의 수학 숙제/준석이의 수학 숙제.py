f=lambda v:n//v*(n//v+1)//2*v
for n in[*open(0)][1].split():n=int(n);print(f(3)+f(7)-f(21))
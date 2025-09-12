n,a,b=map(int,open(0))
c=2*b//n*n
print(*[x:=min(b,c-a),a,c-x,a][2*a//n*n==c::2])
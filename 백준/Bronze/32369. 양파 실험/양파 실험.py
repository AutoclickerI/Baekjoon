N,A,B=map(int,input().split())
c=b=1
exec('b,c=sorted([c+A,b+B]);b-=b==c;'*N)
print(c,b)
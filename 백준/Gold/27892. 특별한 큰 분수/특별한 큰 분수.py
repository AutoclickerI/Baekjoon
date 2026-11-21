x,N=map(int,input().split())
exec('x=x*2//(3*(1-x%2)+1)^6;'*(min(N%12+1200,N)))
print(x)
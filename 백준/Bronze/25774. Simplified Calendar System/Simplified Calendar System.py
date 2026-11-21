d,m,y,n,a,b,c=map(int,open(0).read().split())
print(((c-y)*3+(b-m)*2+a-d+n-1)%7+1)
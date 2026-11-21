m,s,x,X=map(int,input().split())
print(a:=(x-X)*pow(s-x,m-2,m)%m,(x-a*s)%m)
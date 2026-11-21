m,s,x,y=map(int,input().split())
print(a:=(x-y)*pow(s-x,m-2)%m,(x-a*s)%m)
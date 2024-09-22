a,b,c=map(int,input().split())
print([-1,round((((a*a-c*c)*(a*a-b*b))**.5-b*c)/a)][a*a>b*b+c*c])
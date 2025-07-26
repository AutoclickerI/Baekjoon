A,a,B,b,P=map(int,input().split())
print('YNeos'[(a<B or P<A)*(b<A or P<B)*(P<A+B)::2])
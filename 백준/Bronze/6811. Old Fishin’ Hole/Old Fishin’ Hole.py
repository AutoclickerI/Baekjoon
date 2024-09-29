a,b,c,d=map(int,open(0))
R=range(101)
print('Number of ways to catch fish:',len([print(i,'Brown Trout,',j,'Northern Pike,',k,'Yellow Pickerel')for i in R for j in R for k in R if 0<i*a+b*j+c*k<=d]))
x,y,z,n=map(int,input().split())
t=z/n
for i in range(n):
    print(0,0,t*i,x,y,t*-~i)
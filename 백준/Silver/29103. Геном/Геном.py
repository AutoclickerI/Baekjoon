x,y,_,k=map(int,input().split())
print([x-y,y-x][k%2])
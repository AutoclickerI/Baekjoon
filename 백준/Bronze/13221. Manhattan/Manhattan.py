[x,y],n,*p=(map(int,i.split())for i in open(0))
print(*min([abs(i-x)+abs(j-y),i,j]for i,j in p)[1:])
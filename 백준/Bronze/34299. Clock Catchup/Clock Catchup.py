def I():a,b,c=map(int,input().split(':'));return(a*60+b)*60+c+1
R=range(I(),I())
print(*map(lambda i:sum(j%i<1for j in R),(43200,3600,60)))
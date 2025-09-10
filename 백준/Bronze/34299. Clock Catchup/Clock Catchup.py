def I():a,b,c=map(int,input().split(':'));return(a*60+b)*60+c
R=range(I()+1,I()+1)
print(*map(lambda i:sum(j%i<1for j in R),(43200,3600,60)))
R=range(-999,1000)
a,b,c,d,e,f=map(int,input().split())
print(*[[i,j]for i in R for j in R if a*i+b*j==c and d*i+e*j==f][0])
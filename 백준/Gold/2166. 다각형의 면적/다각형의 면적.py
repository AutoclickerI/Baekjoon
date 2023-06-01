n=int(input())
D=[list(map(int,input().split()))for i in[0]*n]
D+=[D[a:=0]]
for i in range(n):a=a+D[i][0]*D[i+1][1]-D[i+1][0]*D[i][1]
print(abs(a/2))
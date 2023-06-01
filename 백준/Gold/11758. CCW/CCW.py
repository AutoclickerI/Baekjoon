D=[list(map(int,input().split()))for i in[0]*3]
D+=[D[(a:=0)]]
for i in range(3):a=a+D[i][0]*D[i+1][1]-D[i+1][0]*D[i][1]
print(1 if a>0 else -1 if a<0 else 0)
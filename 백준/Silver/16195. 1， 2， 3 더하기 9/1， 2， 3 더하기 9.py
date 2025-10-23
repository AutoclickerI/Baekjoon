R=range(1000)
t=[1001*[0]for _ in[0]*1001]
t[0][0]=1
for i in R:
 for j in R:t[i+1][j+1]=t[i][j]+t[i-1][j]+t[i-2][j]
for i in[*open(0)][1:]:n,m=map(int,i.split());print(sum(t[n][:m+1])%(10**9+9))
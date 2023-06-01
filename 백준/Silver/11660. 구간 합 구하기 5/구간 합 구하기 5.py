import sys
I=lambda:map(int,sys.stdin.readline().split())
p,q=I()
l=[[*I()]for _ in[0]*p]
p+=1
l2=[[0]*p for _ in[0]*p]
l2[0][0]=l[0][0]
for i in range(2,p):l2[i][1]=l[i-1][0]+l2[i-1][1];l2[1][i]=l[0][i-1]+l2[1][i-1]
for i in range(2,p):
    for j in range(2,p):l2[i][j]=l[i-1][j-1]+l2[i-1][j]+l2[i][j-1]-l2[i-1][j-1]
for _ in[0]*q:
    r,s,t,u=I()
    print(l2[t][u]-l2[t][s-1]-l2[r-1][u]+l2[r-1][s-1])
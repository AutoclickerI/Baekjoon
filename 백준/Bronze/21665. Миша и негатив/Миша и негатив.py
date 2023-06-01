a,b=map(int,input().split())
p=[input()for i in[0]*a]
input()
q=[input()for i in[0]*a]
print(sum([sum([p[i][j]==q[i][j]for j in range(b)])for i in range(a)]))
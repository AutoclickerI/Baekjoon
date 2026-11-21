I=lambda:map(int,input().split())
R,C=map(range,I())
m=[[*I()]for i in R]
print(min(sum(m[v][w]*min(abs(v-i),abs(w-j))for v in R for w in C)for i in R for j in C))
A,B,C=map(int,input().split())
l=[[]for _ in[0]*10]
for i in range(100):i,j=i//10,i%10+1;l[i]+=[j]*(j*B-~i*A==C)
for i in l:print(*i or[0])
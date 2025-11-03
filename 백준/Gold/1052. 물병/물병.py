N,K=map(int,input().split())
i=N
while K<i.bit_count():i+=1
print(i-N)
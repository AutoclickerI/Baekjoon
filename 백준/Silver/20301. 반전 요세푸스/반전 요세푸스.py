n,k,m=map(int,input().split())
*q,=range(n)
j=r=0
while q:print(1+q.pop(j:=(j-[1-k,k][r//m%2])%len(q)));r+=1
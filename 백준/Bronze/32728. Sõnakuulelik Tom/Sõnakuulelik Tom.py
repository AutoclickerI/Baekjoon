N,K=map(int,input().split())
l=['','','']
for i in input():
    idx='srp'.find(i)-3
    while len(l[idx])==K:idx+=1
    l[idx]+=i
print(*l,sep='\n')
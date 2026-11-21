N,K=map(int,input().split())
*l,=map(int,input().split())
step=0
for i in range(N-1):
    if l[i]<l[i+1]:
        continue
    l[i+1]+=K
    step+=1
if all(i<j for i,j in zip(l,l[1:])):
    print(step)
else:
    print(-1)
k=int(input().split()[1])
s=0
for c in input():t=c!='LR'[s];k-=t;s^=1-t
print(max(0,k))
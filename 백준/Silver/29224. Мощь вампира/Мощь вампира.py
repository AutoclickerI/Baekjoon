n=int(input())
q=['+']*n
print(*q)
a=[int(input())]
for i in range(1,n):q[i-1],q[i]='+','-';print(*q);a+=(a[0]-int(input()))//2,
a[0]-=sum(a[1:])
print('answer:',*a)
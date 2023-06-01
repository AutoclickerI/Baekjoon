input()
a,*l=map(int,input().split())
A=[0,0]
for i in l:A[i>a]+=abs(a-i);a=i
print(*A)
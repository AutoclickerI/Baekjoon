T=int(input())
input()
A=[0]
for i in input().split():A+=A[-1]+int(i),
dA={}
for i in range(len(A)):
    for j in range(i+1,len(A)):
        v=A[j]-A[i]
        dA[v]=dA.get(v,0)+1
input()
B=[0]
for i in input().split():B+=B[-1]+int(i),
a=0
for i in range(len(B)):
    for j in range(i+1,len(B)):
        a+=dA.get(T+B[i]-B[j],0)
print(a)
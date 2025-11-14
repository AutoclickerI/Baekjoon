T=int(input())
input()
A=[0]
for i in input().split():
    A+=A[-1]+int(i),
dA={}
for i in range(len(A)):
    for j in range(i+1,len(A)):
        v=A[j]-A[i]
        dA[v]=dA.get(v,0)+1
input()
B=[0]
for i in input().split():
    B+=B[-1]+int(i),
dB={}
for i in range(len(B)):
    for j in range(i+1,len(B)):
        v=B[j]-B[i]
        dB[v]=dB.get(v,0)+1
a=0
for v in dB:
    a+=dA.get(T-v,0)*dB[v]
print(a)
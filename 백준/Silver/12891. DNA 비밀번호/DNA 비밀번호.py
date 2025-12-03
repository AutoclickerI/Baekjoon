I=lambda:map(int,input().split())
S,P=I()
X=input()
R=0
Q=dict(zip('ACGT',I()))
for i in range(S):Q[X[i]]-=1;Q[X[i-P]]+=P<=i;R+=max(Q.values())<1>P+~i
print(R)
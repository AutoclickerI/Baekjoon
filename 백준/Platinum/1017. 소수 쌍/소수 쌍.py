R=range
l=[*R(2002)]
for i in R(2002)[2:]:
    a=i
    if l[i]:
        while(a:=a+i)<2002:l[a]=0
p,*n=map(int,open(0).read().split())
n=n[::-1]
N=[[]for _ in[0]*p]
for i in R(p):
    for j in R(p):N[i]+=[j]*((i-j)*l[n[i]+n[j]]and 1)
E=[-1]*p
S=[-1]*p
a=[]
def DFS(n):
    V[n]=1
    for i in N[n]:
        if -1==E[i]or~-V[E[i]]and DFS(E[i]):E[i]=n;S[n]=i;return 1
    return 0
F=1
for i in R(p-1):
    if -1==S[i]:V=[0]*p;F=min(DFS(i),F)
B=[*E],[*S]
for i in N[-1]:
    V=[0]*p
    if -1==E[i]or~-V[E[i]]and DFS(E[i]):E,S=B;B=[*E],[*S];a+=[n[i]]
print(*sorted(a)if F*a else[-1])
def to_int(s):
    C,C_b=s.split('.')
    return C+C_b+'0'*(9-len(C_b))

L,C,S=input().split()
C=to_int(C)

L,C,S=map(int,[L,C,S])
E,M=map(int,input().split())
C_max,C_min=map(int,map(to_int,input().split()))

def step(C,L,S):
    return C*L//(L+M),L+M,S-M

def drink(C,L,S):
    while S and C_max<C:
        C,L,S=step(C,L,S)
    a=0
    if C_max<C:
        return a
    while S and C_min<=C:
        a+=min(L,E)
        L-=min(L,E)
        C,L,S=step(C,L,S)
    if C_min<=C:
        a+=L
    return a

l=[(C,L,S)]
while S:
    x=C,L,S=step(C,L,S)
    l+=x,
m=0
for i in range(len(l)-1):
    if C_max<l[i+1][0]:
        m=i
l=l[m:]

while l and l[-1][0]<C_min:
    l.pop()

l+=x,

s=0
e=len(l)-1

while s+2<e:
    a=(s*2+e)//3
    b=(s+e*2)//3
    if drink(*l[b])<=drink(*l[a]):
        e=b
    else:
        s=a
print(max([drink(*l[i])for i in range(max(s-100,0),min(s+100,len(l)))]+[drink(*l[-1])]))
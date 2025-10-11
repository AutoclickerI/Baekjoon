S,P=map(int,input().split())
s=input()
*c,=map(s[:P].count,'ACGT')
*C,=map(int,input().split())
v=all(j<=i for i,j in zip(c,C))
for i in range(S-P):
    c['ACG'.find(s[i])]-=1
    c['ACG'.find(s[i+P])]+=1
    v+=all(j<=i for i,j in zip(c,C))
print(+v)
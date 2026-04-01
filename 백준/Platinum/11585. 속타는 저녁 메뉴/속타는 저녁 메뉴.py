N=int(input())
T=input().split()*2
T.pop()
s=input().split()

pi=[0]

j=0
for i in range(1,len(s)):
    while j and s[i]!=s[j]:
        j=pi[j-1]
    if s[i]==s[j]:
        j+=1
    pi+=j,

r=0
j=0

for i in range(len(T)):
    while j and T[i]!=s[j]:
        j=pi[j-1]
    if T[i]==s[j]:
        if j==len(s)-1:
            r+=1
            j=pi[j]
        else:
            j+=1

import math
gcd=math.gcd(N,r)
print(f'{r//gcd}/{N//gcd}')
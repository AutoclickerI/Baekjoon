T=input()
s=input()

pi=[0]

j=0
for i in range(1,len(s)):
    while j and s[i]!=s[j]:
        j=pi[j-1]
    if s[i]==s[j]:
        j+=1
    pi+=j,

ans=[]
j=0

for i in range(len(T)):
    while j and T[i]!=s[j]:
        j=pi[j-1]
    if T[i]==s[j]:
        if j==len(s)-1:
            ans+=i-len(s)+2,
            j=pi[j]
        else:
            j+=1
print(len(ans))
print(*ans)
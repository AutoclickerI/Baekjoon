o=input()
m=0
for i in range(len(o)):
    s=o[i:]
    pi=[0]
    j=0
    for i in range(1,len(s)):
        while j and s[i]!=s[j]:
            j=pi[j-1]
        if s[i]==s[j]:
            j+=1
        pi+=j,
    m=max(m,max(pi))
print(m)
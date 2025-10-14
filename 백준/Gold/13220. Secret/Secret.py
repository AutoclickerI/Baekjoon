_,T,s=map(str.split,open(0))
T*=2

pi=[0]
j=0
for i in range(1,len(s)):
    while j and s[i]!=s[j]:
        j=pi[j-1]
    if s[i]==s[j]:
        j+=1
    pi+=j,

j=0
for i in range(len(T)):
    while j and T[i]!=s[j]:
        j=pi[j-1]
    if T[i]==s[j]:
        if j==len(s)-1:
            print('YES')
            break
        else:
            j+=1
else:
    print('NO')
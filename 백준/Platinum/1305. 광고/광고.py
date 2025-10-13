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

print(len(s)-pi[-1])
input()
s=input()
i=s[:2]
for j in range(2,len(s)-1):
    if i!=s[j:j+2]:
        print('Yes')
        exit(print(1,j+1,2))
print('No')
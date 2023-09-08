s = input()
ans=0
for i in range(1, len(s)+1):
    subset = set()
    for j in range(len(s)-i+1):
        subset.add(s[j:j+i])
    ans+=len(subset)
print(ans)
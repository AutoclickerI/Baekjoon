d={' ':1}
for _ in[0]*int(input()):
    *s,=input()
    l=[0]
    for i in range(len(s)):
        if s[i-1]==' ':
            l+=i,
    for i in l:
        if s[i].lower()not in d:
            d[s[i].lower()]=1
            s[:i]+='['
            s[:i+2]+=']'
            break
    else:
        for i in range(len(s)):
            if s[i].lower()not in d:
                d[s[i].lower()]=1
                s[:i]+='['
                s[:i+2]+=']'
                break
    print(*s,sep='')
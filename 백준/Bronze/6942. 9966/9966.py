ans= 0
m, n =int(input()),int(input())
for s in map(str,range(m, n + 1)):
    flag = 1
    for i in range((len(s) + 1) >> 1):
        if s[i] not in '01698':
            flag = False
            break
        if s[i] in '018':
            if s[i] == s[-(i+1)]:continue
            else:
                flag = 0;break
        if s[i]+s[-(i+1)]not in('69','96'):
            flag =0;break
    ans += flag
print(ans)
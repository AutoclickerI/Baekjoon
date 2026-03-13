def sup(s):
    for i in range(1,len(s)):
        v={}
        for j in range(i,len(s)):
            t=s[j-i]+s[j]
            if t in v:
                return 0
            v[t]=1
    return 1

for i in[*open(0)][:-1]:
    i=i[:-1]
    print(i,'is','NOT surprising.'[sup(i)*4:])
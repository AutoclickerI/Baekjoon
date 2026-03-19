def check(n):
    if n==1:
        return 0
    v=n//2
    for i in range(v):
        if s[i]==s[n-1-i]:
            return 1
    return check(v)

for s in[*open(0)][1:]:
    print('YNEOS'[check(len(s)-1)::2])
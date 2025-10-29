def check(s):
    for i in range(1,len(s)//2+1):
        for offset in range(i):
            *cks,=zip(*[iter(s[offset:])]*i)
            for p,q in zip(cks,cks[1:]):
                if p==q:return 0
    return 1


def backtrack(s):
    if check(s):
        if len(s)==n:
            exit(print(s))
        for i in'123':
            backtrack(s+i)

n=int(input())
backtrack('')
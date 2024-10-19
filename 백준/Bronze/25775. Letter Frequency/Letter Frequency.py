l=[*open(0)][1:]
m=max(map(len,l))
def get(n):
    return[i[n]for i in l if n<len(i)]
for i in range(m-1):
    z=[]
    s=get(i)
    n=0
    for c in range(97,123):
        if n<s.count(chr(c)):
            z=[chr(c)]
            n=s.count(chr(c))
        elif n==s.count(chr(c)):
            z+=chr(c),
    print(f'{i+1}:',*z)
for _ in[0]*int(input()):
    input()
    pw=input()
    s=input()
    for i in range(len(pw)+1):
        if pw[:i]==s[:i]:
            pos=i
    if pos==len(s):
        print(pw[pos:]+'*')
    if pos<len(s):
        print(min('*'+pw,'<'*(len(s)-pos)+pw[pos:],key=len)+'*')
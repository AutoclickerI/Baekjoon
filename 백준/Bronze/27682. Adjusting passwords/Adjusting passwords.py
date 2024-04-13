for _ in[0]*int(input()):
    input()
    pw=input()
    s=input()
    pos=max(i*(pw[:i]==s[:i])for i in range(len(pw)+1))
    print(min('*'+pw,'<'*(len(s)-pos)+pw[pos:],key=len)+'*')
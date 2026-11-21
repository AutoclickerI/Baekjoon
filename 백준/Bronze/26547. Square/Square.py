for _ in[0]*int(input()):
    *s,=input()
    l=[s]+[' '*len(s)]*(len(s)-2)+[s[::-1]]
    *l,=zip(*l)
    l[0]=s;l[-1]=s[::-1]
    for i in l:print(*i,sep='')
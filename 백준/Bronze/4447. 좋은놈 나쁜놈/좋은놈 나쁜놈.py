def c(s):
    g,b=map(s.count,'gb')
    if g==b:
        return'NEUTRAL'
    if b<g:
        return'GOOD'
    return'A BADDY'
for _ in[0]*int(input()):
    s=input()
    print(s,'is',c(s.lower()))
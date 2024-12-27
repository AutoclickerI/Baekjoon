v=0
while 1:
    s=input()
    if s=='#':
        break
    if s=='0':
        print(v)
        v=0
    else:
        _,_,c,t=s.split()
        if t=='F':
            v+=2*int(c)
        elif t=='B':
            v+=int(c)*3+1>>1
        else:
            v+=max(int(c),500)
input()
r=S=L=0
for c in input():
    if c<':':
        r+=1
    elif c=='S':
        S+=1
    elif c=='L':
        L+=1
    elif c=='K':
        if S:
            S-=1
            r+=1
        else:
            break
    elif c=='R':
        if L:
            L-=1
            r+=1
        else:
            break
print(r)
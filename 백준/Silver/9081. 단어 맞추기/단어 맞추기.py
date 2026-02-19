for _ in[0]*int(input()):
    s=input()
    for i in range(len(s))[::-1]:
        if s[i]!=max(s[i:]):
            c=min(j for j in s[i:]if s[i]<j)
            z=sorted(s[i:])
            del z[z.index(c)]
            print(s[:i]+c+''.join(z))
            break
    else:
        print(s)
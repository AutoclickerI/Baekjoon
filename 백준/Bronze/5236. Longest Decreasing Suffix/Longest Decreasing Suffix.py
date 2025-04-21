for _ in[0]*int(input()):
    s=input()
    for i in range(len(s)):
        if s[i:]==''.join(sorted(s[i:])[::-1]):
            print('The longest decreasing suffix of',s,'is',s[i:])
            break
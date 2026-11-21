for s in[*open(0)][1:]:
    b=' '
    for i in range(len(s)-1):
        if s[i]in':-':b+=' '*(b[-1]!=' ')+s[i]+' '*(i!=len(s)-2!=' '!=s[i+1])
        else:b+=s[i]
    print(b[1:])
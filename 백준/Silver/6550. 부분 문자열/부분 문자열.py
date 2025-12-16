for i in open(0):
    s,e=i.split()
    i=0
    s+='.'
    for c in e:
        i+=s[i]==c
    print('YNeos'[s[i]!='.'::2])
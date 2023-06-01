a=list(input())
b=[]
d={'*':2,'/':2,'+':1,'-':1}
for k in a:
    if k.isalpha():
        print(k,end='')
    else:
        if k=='(':
            b.append(k)
        else:
            if k==')':
                while b[-1]!='(':
                    print(b.pop(),end='')
                b.pop()
            else:
                if len(b)==0:
                    b.append(k)
                else:
                    if b[-1]=='(':
                        b.append(k)
                    elif d[b[-1]]<d[k]:
                        b.append(k)
                    else:
                        print(b.pop(),end='')
                        if len(b)==0:
                            b.append(k)
                        else:
                            if b[-1]=='(':
                                b.append(k)
                            elif d[b[-1]]==d[k]:
                                print(b.pop(),end='')
                                b.append(k)
                            else:
                                b.append(k)
print(*reversed(b),sep='')
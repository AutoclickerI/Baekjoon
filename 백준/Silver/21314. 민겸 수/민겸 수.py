s=input()

def m(s):
    r=[]
    st=[]
    for i in s:
        if i=='K':
            if st:
                r+=str(10**(len(st)-1))
                st=[]
            r+='5'
        else:
            st+=i
    if st:
        r+=str(10**(len(st)-1))
    return''.join(r)

def M(s):
    r=[]
    st=[]
    for i in s:
        if i=='K':
            r+=str(5*10**len(st))
            st=[]
        else:
            st+=i
    if st:
        r+='1'*len(st)
    return''.join(r)

print(M(s),m(s))
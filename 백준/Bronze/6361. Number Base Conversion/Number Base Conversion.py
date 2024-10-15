def to_b(n,b):
    if n==0:
        return'0'
    else:
        s=''
        while n:
            s='0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'[n%b]+s
            n//=b
        return s
def to_10(s,b):
    v=0
    for i in s:
        v*=b
        v+='0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'.find(i)
    return v
for i in[*open(0)][1:]:
    a,b,c=i.split()
    print(a,c)
    print(b,to_b(to_10(c,int(a)),int(b)))
    print()
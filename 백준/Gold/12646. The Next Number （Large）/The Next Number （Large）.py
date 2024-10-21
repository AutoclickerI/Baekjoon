for T in range(int(input())):
    *l,=input()
    a=[]
    while l:
        if l[1:]==sorted(l[1:])[::-1]:
            if l[0]==max(l):
                a+=min(i for i in l if i!='0')
                l.remove(a[-1])
                a+='0',*sorted(l)
                l=[]
            else:
                c=min(i for i in l if l[0]<i)
                a+=c
                l.remove(c)
                a+=sorted(l)
                l=[]
        else:
            a+=l.pop(0)
    print(f'Case #{T+1}:',''.join(a))
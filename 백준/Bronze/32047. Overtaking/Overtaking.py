while'0'<input():
    *l1,=map(int,input().split())
    *l2,=map(int,input().split())
    a=0
    ptr=0
    while ptr<len(l1)and l1[ptr]==l2[ptr]:
        ptr+=1
    if ptr<len(l1):
        s1=l1[ptr];s2=l2[ptr]
        f=s1<s2
        ptr+=1
        while ptr<len(l1):
            s1+=l1[ptr]
            s2+=l2[ptr]
            if s1!=s2 and (s1<s2)!=f:
                a+=1
                f^=1
            ptr+=1
    print(a)
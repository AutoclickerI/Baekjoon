for i in[*open(0)][1:]:
    mv=float('inf')
    p=q=r=s=e=0
    while s<=e:
        f=0
        while e<len(i)and p*q*r<1:
            p+=i[e].isupper()
            q+=i[e].islower()
            r+=i[e].isdigit()
            e+=1
            f=1
        while s<=e and p*q*r:
            if 5<e-s:
                mv=min(mv,e-s)
            p-=i[s].isupper()
            q-=i[s].islower()
            r-=i[s].isdigit()
            s+=1
            f=1
        if f<1:break
        
    print(mv if mv!=float('inf')else 0)
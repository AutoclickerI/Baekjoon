for idx in range(int(input())):
    input()
    *l,=input().split()
    a=0
    for i in range(1,len(l)):
        if int(l[i-1])<int(l[i]):
            pass
        elif l[i-1][:len(l[i])]<l[i]:
            a+=len(l[i-1])-len(l[i])
            l[i]+='0'*(len(l[i-1])-len(l[i]))
        elif l[i-1][:len(l[i])]==l[i]:
            s=str(int(l[i-1])+1)
            if s.startswith(l[i]):
                a+=len(s)-len(l[i])
                l[i]=s
            else:
                a+=len(l[i-1])-len(l[i])+1
                l[i]+='0'*(len(l[i-1])-len(l[i])+1)
        else:
            a+=len(l[i-1])-len(l[i])+1
            l[i]+='0'*(len(l[i-1])-len(l[i])+1)
    print(f'Case #{idx+1}:',a)
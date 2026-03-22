T=0
while n:=int(input()):
    T+=1
    f=1
    print('Group',T)
    l=[input().split()for _ in[0]*n]
    for i in range(n):
        s,*r=l[i]
        for j in range(n-1):
            if r[j]=='N':
                print(l[i-j-1][0],'was nasty about',s)
                f=0
    print('Nobody was nasty\n'*f)
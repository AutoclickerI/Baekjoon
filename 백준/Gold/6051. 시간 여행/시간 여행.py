l=[(-1,-1)]
ptr=0
for _ in[0]*int(input()):
    t=input().split()
    if t[0]=='a':
        l+=(t[1],ptr),
        ptr=len(l)-1
    if t[0]=='s':
        ptr=l[-1][1]
        l+=l[ptr],
    if t[0]=='t':
        ptr=int(t[1])-1
        l+=l[ptr],
    print(l[ptr][0])
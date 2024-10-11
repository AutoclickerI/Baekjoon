for a in[0]*int(input()):
    w=int(input())
    c=-1
    for i in input().split():
        t=c+len(i)+1
        if t==w:a+=1;c=-1
        elif t>w:a+=1;c=len(i)
        else:c=t
    print(a+(0<=c))
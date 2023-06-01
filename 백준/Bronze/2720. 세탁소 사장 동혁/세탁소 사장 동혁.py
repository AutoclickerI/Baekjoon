l=[25,10,5,1]
for _ in[0]*int(input()):
    p=int(input())
    for i in l:
        print(p//i,end=' ')
        p%=i
for _ in[0]*int(input()):
    l=bin(int(input()))[2:][::-1]
    for i in range(len(l)):
        if int(l[i]):print(i,end=' ')
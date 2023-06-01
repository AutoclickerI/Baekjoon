for _ in[0]*int(input()):
    s=q=0
    for _ in[0]*int(input()):
        a,b=input().split()
        if a=='R':
            if b=='P':q+=1
            elif b=='S':s+=1
        elif a=='P':
            if b=='S':q+=1
            elif b=='R':s+=1
        else:
            if b=='R':q+=1
            elif b=='P':s+=1
    print('Player 1'if s>q else'Player 2'if s<q else'TIE')
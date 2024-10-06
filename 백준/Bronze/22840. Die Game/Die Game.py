while n:=int(input()):
    top,north,west=1,2,3
    for _ in range(n):
        cmd=input()[0]
        if cmd=='n':top,north=7-north,top
        elif cmd=='s':top,north=north,7-top
        elif cmd=='e':top,west=west,7-top
        else:top,west=7-west,top
    print(top)
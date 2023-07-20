for _ in[0]*int(input()):
    p,q=map(int,input().split())
    bmi=10000*q/p/p
    if p<141:
        print(6)
    elif p<146:
        print(5)
    elif p<159:
        print(4)
    elif p<161:
        print(4-(16<=bmi<35))
    elif p<204:
        if 20<=bmi<25:
            print(1)
        elif 18.5<=bmi<20 or 25<=bmi<30:
            print(2)
        elif 16<=bmi<18.5 or 30<=bmi<35:
            print(3)
        else:
            print(4)
    else:
        print(4)
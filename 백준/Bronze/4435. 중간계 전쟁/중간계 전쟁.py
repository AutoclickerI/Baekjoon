for i in range(int(input())):
    a,b,c,d,e,f=map(int,input().split())
    G=a+b*2+c*3+d*3+e*4+f*10
    a,b,c,d,e,f,g=map(int,input().split())
    S=a+b*2+c*2+d*2+e*3+f*5+g*10
    print(f'Battle {i+1}:','Evil eradicates all trace of Good'if G<S else'Good triumphs over Evil'if G>S else'No victor on this battle field')
for i in range(int(input())):
    
    R,P,D=map(int,input().split())
    l=[input().split()for _ in[0]*R]
    m=eval([*filter(lambda x:x[2]=='100.0',l)][0][1])*D/P
    print('Recipe #',i+1)
    for p,_,q in l:
        print(p,f'{m*eval(q)/100:.1f}')
    print('----------------------------------------')
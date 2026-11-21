for _ in[0]*int(input()):
    p,q=map(float,input().split())
    print(f'{int(abs(p-q)*10+.5)/10:.1f}')
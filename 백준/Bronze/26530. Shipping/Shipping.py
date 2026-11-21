for _ in[0]*int(input()):
    a=0
    for _ in[0]*int(input()):
        p,q,r=input().split()
        a+=eval(q+'*'+r)
    print(f'${a:.2f}')
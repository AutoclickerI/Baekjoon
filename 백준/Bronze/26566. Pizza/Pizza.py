for _ in[0]*int(input()):
    p,q=map(int,input().split())
    r,s=map(int,input().split())
    if p/q>r*r*3.141592/s:print('Slice of pizza')
    else:print('Whole pizza')
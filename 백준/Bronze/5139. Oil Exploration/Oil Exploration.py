for i in range(int(input())):
    h,w=map(int,input().split())
    print(f'Data Set {i+1}:')
    for i in zip(*eval('input(),'*h)):
        idx=''.join(i).find('X')
        if idx<0:print(end='N ')
        else:print(sum(1+2*(t=='H')for t in i[:idx]),end=' ')
    print('\n')
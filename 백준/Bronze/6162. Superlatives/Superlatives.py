for i in range(int(input())):
    p,q=map(int,input().split())
    p-=1
    print(f'Data Set {i+1}:')
    if p<q:
        print(end='no ')
    else:
        while(p:=p//5)>q:
            print(end='mega ')
    print('drought\n')
i=0
while(s:=input())>'1':
    i+=1
    p,a=map(int,s.split())
    print(f'Hole #{i}')
    if a==1:
        print('Hole-in-one.')
    elif p==a:
        print('Par.')
    elif p-a==1:
        print('Birdie.')
    elif p-a==2:
        print('Eagle.')
    elif p-a==3:
        print('Double eagle.')
    elif a-p==1:
        print('Bogey.')
    elif a-p>1:
        print('Double Bogey.')
    print()
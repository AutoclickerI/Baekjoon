a=int(input())
b=int(input())
if a>2:
    print('After')
if a<2:
    print('Before')
if a==2:
    if b>18:
        print('After')
    elif b<18:
        print('Before')
    else:
        print('Special')
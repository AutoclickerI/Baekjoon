if int(input())<51:
    if(l:=int(input()))<11:
        print('White')
    elif l<31:
        print('Yellow')
    else:print('Red')
else:
    if int(input())<31:
        print('Yellow')
    else:
        print('Red')
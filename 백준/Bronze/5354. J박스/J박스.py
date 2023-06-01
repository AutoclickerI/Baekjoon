for i in[0]*int(input()):
    l=int(input())
    if l==1:print('#\n')
    else:
        print('#'+'#'*(l-2)+'#')
        print(('#'+'J'*(l-2)+'#\n')*(l-2),end='')
        print('#'+'#'*(l-2)+'#\n')
while int(i:=input()):
    *i,=i
    if int(i[i.index(max(i))])%2:
        i[i.index(max(i))]='0'
    else:
        i[i.index(max(i))]=str((int(i[i.index(max(i))])+4)%10)
    print(int(''.join(i)))
for s in[0]*int(input()):
    i,j=input().split('-')
    for c in i:s*=26;s+=ord(c)-65
    print('not '*(100<abs(int(j)-s))+'nice')
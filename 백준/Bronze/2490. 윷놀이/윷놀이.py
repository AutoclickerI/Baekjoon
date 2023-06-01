for i in range(3):
    a=input().split();a.sort()
    print('D'if a[3]=='0' else'C'if a[2]=='0'else'B' if a[1]=='0'else'A'if a[0]=='0'else'E')
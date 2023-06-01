while s:=input():
    if s.isdigit():s=='0' and exit();continue
    l=[i<128 for i in map(int,s.split())]
    print('*'if sum(l)-1 else chr(65+l.index(1)))
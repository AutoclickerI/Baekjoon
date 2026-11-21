while s:=input():
 if s.isdigit():s=='0' and exit();continue
 print('*'if sum(l:=[i<128 for i in map(int,s.split())])-1 else chr(65+l.index(1)))
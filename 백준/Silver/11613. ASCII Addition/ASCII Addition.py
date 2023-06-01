l=[input()+'.'for _ in[0]*7]
d={('....x.', '....x.', '....x.', '....x.', '....x.', '....x.', '....x.'): '1',
 ('xxxxx.', '....x.', '....x.', 'xxxxx.', 'x.....', 'x.....', 'xxxxx.'): '2',
 ('xxxxx.', '....x.', '....x.', 'xxxxx.', '....x.', '....x.', 'xxxxx.'): '3',
 ('x...x.', 'x...x.', 'x...x.', 'xxxxx.', '....x.', '....x.', '....x.'): '4',
 ('xxxxx.', 'x.....', 'x.....', 'xxxxx.', '....x.', '....x.', 'xxxxx.'): '5',
 ('xxxxx.', 'x.....', 'x.....', 'xxxxx.', 'x...x.', 'x...x.', 'xxxxx.'): '6',
 ('xxxxx.', '....x.', '....x.', '....x.', '....x.', '....x.', '....x.'): '7',
 ('......', '..x...', '..x...', 'xxxxx.', '..x...', '..x...', '......'): '+',
 ('xxxxx.', 'x...x.', 'x...x.', 'xxxxx.', 'x...x.', 'x...x.', 'xxxxx.'): '8',
 ('xxxxx.', 'x...x.', 'x...x.', 'xxxxx.', '....x.', '....x.', 'xxxxx.'): '9',
 ('xxxxx.', 'x...x.', 'x...x.', 'x...x.', 'x...x.', 'x...x.', 'xxxxx.'): '0'}
n=str(eval(''.join(d[tuple(i[6*j:6*j+6]for i in l)]for j in range(len(l[0])//6))))
li=[]
for i in n:
    for j in d:
        if d[j]==i:li+=[j]
[print(''.join(i)[:-1])for i in zip(*li)]
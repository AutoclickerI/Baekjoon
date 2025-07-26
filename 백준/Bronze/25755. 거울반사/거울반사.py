[w,*_],*l=[i.translate(str.maketrans('2534679','52?????')).split()for i in open(0)]

if w in'UD':
    l=l[::-1]
else:
    l=[i[::-1]for i in l]

for i in l:
    print(*i)
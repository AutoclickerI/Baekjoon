_,*l=open(0)
l+=map(''.join,zip(*l))
l.pop()
print(int(all(len(l)==i.count('B')*4and'BBB'not in i and'WWW'not in i for i in l)))
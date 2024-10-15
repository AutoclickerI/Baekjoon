n=int(input())
*l,=eval('input(),'*n)
l+=map(''.join,zip(*l))
print(int(all(len(l)==i.count('B')*4and'BBB'not in i and'WWW'not in i for i in l)))
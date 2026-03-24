_,*s=open(0)
*s,=map(''.join,zip(*s))
N=len(s)
c=0
while len({i[c:]for i in s})==N:c+=1
print(c-1)
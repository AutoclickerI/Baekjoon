M,*l=open(s:=0)
e=9**19
while-~s<e:m=s+e>>1;s,e=(s,m,m,e)[sum(m//int(i)for i in l)<int(M.split()[1])::2]
print(e)
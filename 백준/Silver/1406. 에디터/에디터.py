(*s,_),_,*c=open(0)
t=[]
for i in c:
 if'L'in i and s:t+=s.pop()
 if'D'in i and t:s+=t.pop()
 if'C'>i:del s[-1:]
 if'P'<i:s+=i[2]
print(*s+t[::-1],sep='')
s=[]
for i in[*open(0)][1:]:
 if i=='READ\n':print(end=s.pop())
 else:s+=i,
_,s=open(0)
i=1
while s.startswith(''.join(map(str,range(1,i+1)))):i+=1
print(i)
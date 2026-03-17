_,*l=open(0)
p=''.join
for i in range(5):print(p(map(p,zip(*l))).count('*'*i+'.'*(4-i))>>2)
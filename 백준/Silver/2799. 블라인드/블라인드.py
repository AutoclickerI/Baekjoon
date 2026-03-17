_,*l=open(0)
for i in range(5):print(''.join(sum(zip(*l),())).count('*'*i+'.'*(4-i))>>2)
import math
s=['  *  ',' * * ','*****']
for j in range(int(math.log2(int(input())//3))):s=[' '*(3<<j)+i+' '*(3<<j)for i in s]+[i+' '+i for i in s]
print(*s,sep='\n')
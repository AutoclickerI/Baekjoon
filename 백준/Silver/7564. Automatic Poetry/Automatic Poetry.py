import re
I=input
exec("l=re.split('[<>]',I());print(*l,sep='');print(I()[:-3]+l[3]+l[2]+l[1]+l[4]);"*int(I()))
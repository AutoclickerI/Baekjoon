_,*l=open(0)
from collections import*
c=Counter
print('YNeos'[all(len(c(''.join(l))-c(i))>2for i in[*zip(*l)]+l)::2])
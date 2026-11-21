from collections import*
a,b=map(Counter,open(0))
b-=a
print('NA'[len(b)<1or len(b)<2>0<b['*']])
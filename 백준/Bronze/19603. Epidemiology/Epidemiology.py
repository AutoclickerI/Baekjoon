import math
P,N,R=map(int,open(0))
print(R>1 and int(math.log((R*P-P+N)/N,R))or P//N)
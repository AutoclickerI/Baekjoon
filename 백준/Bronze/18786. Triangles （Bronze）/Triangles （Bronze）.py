from itertools import*
print(max(abs(X-Z)*abs(x-y)for(x,X),(y,Y),(z,Z)in permutations([[*map(int,i.split())]for i in open(0)][1:],3)if x==z and X==Y))